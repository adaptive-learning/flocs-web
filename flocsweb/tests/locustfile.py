import random
from json.decoder import JSONDecodeError
from locust import HttpLocust, TaskSet, task


class DoTask(TaskSet):
    """
    This class represents part of the user interaction with server regarding
    task solving. The user requests a randomly choosing task, does some random
    number of unsuccessful tries and then finally solves the task.
    """
    solve_probability = 0.3

    def on_start(self):
        response = self.client.get('/api/tasks/')
        ids = [task['task_id'] for task in response.json()]
        selected_id = random.choice(ids)
        # selected_id = response.json()[0]['task_id']
        self.start_task(selected_id)
        self.edit_program()

    def start_task(self, task_id):
        self.parent.post_with_cookies(
            '/api/actions/',
            {"type": "start-task",
             "data": "{{\"task-id\": \"{}\",\"student_id\": \"{}\"}}"
                 .format(task_id, self.parent.data['student_id']),
             }
        )

    @task(5)
    def edit_program(self):
        required = ['student_id', 'task_session_id']
        for item in required:
            if item not in self.parent.data:
                print("Cannot edit program, {} is missing".format(item))
                self.interrupt()

        self.parent.post_with_cookies(
            '/api/students/{}/edit_program/'.format(
                self.parent.data['student_id']),
            {"task-session-id": self.parent.data['task_session_id'],
             "program": "↑"
             }
        )

    @task(1)
    def run_task(self):
        required = ['student_id', 'task_session_id']
        for item in required:
            if item not in self.parent.data:
                print("Cannot edit program, {} is missing".format(item))
                self.interrupt()

        solved = random.random() < self.solve_probability
        self.parent.post_with_cookies(
            '/api/students/{}/run_program/'.format(
                self.parent.data['student_id']),
            {"task-session-id": self.parent.data['task_session_id'],
             "program": "↑",
             "correct": solved,
             }
        )
        if solved:
            self.interrupt()


class UserBehavior(TaskSet):
    """
    This class represents the whole user interaction with server.
    """

    tasks = [DoTask]

    def __init__(self, parent):
        super().__init__(parent)
        self.cookies = {}
        self.data = {}

    def on_start(self):
        """
        Fills in cookies so that post request can be made later.
        """
        self.index()
        self.start_session()

    def index(self):
        """
        Initial interaction with server. Imitates going to the main page.
        """
        response = self.client.get('/')
        self.save_cookies_and_data(response)

    def start_session(self):
        """
        The session and lazy user is created. Now tasks can be solved.
        """
        self.post_with_cookies('/api/actions/',
                               {"type": "start-session", "data": "{}"}
                               )

    def save_cookies_and_data(self, response):
        """
        Stores cookies for later usage.
        """
        self.cookies.update(response.cookies.get_dict())
        try:
            received_data = response.json().get('data')
            if received_data:
                self.data.update(received_data)
        except JSONDecodeError:
            return

    def post_with_cookies(self, url, data):
        """
        Shortcut for making post request and to having to add all the cookies
        and headers.
        """
        csrf_token = self.cookies['csrftoken']
        data["csrfmiddlewaretoken"] = csrf_token
        response = self.client.post(url, data,
                                    headers={"X-CSRFToken": csrf_token,
                                             "Referer": self.client.base_url},
                                    cookies=self.cookies,
                                    )
        self.save_cookies_and_data(response)
        self.log_errors(response)
        return response

    def log_errors(self, response):
        if not response.ok:
            with open('request_errors.log', 'a') as f:
                f.writelines(response.text)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 500
    max_wait = 5000
