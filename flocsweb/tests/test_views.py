import json
from django.core.management import call_command
from django.test import TestCase
from practice.models import Student


class FlocsWebViewsTests(TestCase):

    def setUp(self):
        call_command('load_static_data')
            # TODO: is it possible to avoid the necessity of calling this command
            # for each test? (maybe create a fixture in advance and only
            # specify the fixture)

    def test_start_session(self):
        """ Anonymous user should be able to start session and obtain student_id
        """
        response = self.client.post(
            '/api/actions/',
            {'type': 'start-session', 'data': '{}'}
        )
        self.assertIsNotNone(response.data['action_id'])
        self.assertEqual(response.data['type'], 'start-session')
        self.assertIsInstance(response.data['data'], dict)
        self.assertIn('student_id', response.data['data'])
        # start session again -> should return the same user and even the session
        response2 = self.client.post(
            '/api/actions/',
            {'type': 'start-session', 'data': '{}'}
        )
        self.assertEqual(response2.data['type'], 'start-session')
        self.assertEqual(response2.data['data'], response.data['data'])

    def test_recommendation(self):
        """Recommendation should not change if the current task was not solved
        """
        # start session
        response = self.client.post(
            '/api/actions/',
            {'type': 'start-session', 'data': '{}'})
        student_id = response.data['data']['student_id']
        # request a recommendation
        response = self.client.get(
            '/api/students/{pk}/practice_overview/'.format(pk=student_id))
        task_id = response.data['recommendation']['task_id']
        self.assertIsNotNone(task_id)
        # start solving recommended task
        response = self.client.post(
            '/api/actions/',
            {'type': 'start-task', 'data': json.dumps({'task_id': task_id})})
        task_session_id = response.data['data']['task_session_id']
        # request recommendation - should be same as the first one
        response = self.client.get(
            '/api/students/{pk}/practice_overview/'.format(pk=student_id))
        task_id2 = response.data['recommendation']['task_id']
        self.assertEqual(task_id, task_id2)
        # solve the task
        response = self.client.post(
            '/api/actions/',
            {'type': 'solve-task', 'data': json.dumps({'task_session_id': str(task_session_id)})})
        # and now get different recommendation
        response = self.client.get(
            '/api/students/{pk}/practice_overview/'.format(pk=student_id))
        task_id3 = response.data['recommendation']['task_id']
        self.assertIsNotNone(task_id3)
        self.assertNotEqual(task_id3, task_id2)

    def test_see_instruction(self):
        """ Create student, see instruction, check seen instructions
        """
        # start session
        response = self.client.post(
            '/api/actions/',
            {'type': 'start-session', 'data': '{}'})
        student_id = response.data['data']['student_id']
        # see instruction
        self.client.post(
            '/api/actions/',
            {'type': 'see-instruction',
             'data': json.dumps({'instruction_id': 'block.shoot'})})
        student = Student.objects.get(pk=student_id)
        seen_instruction_ids = list(instruction.instruction_id
                                    for instruction in student.seen_instructions.all())
        self.assertEqual(seen_instruction_ids, ['block.shoot'])


    def test_solve_task(self):
        # start session
        response = self.client.post(
            '/api/actions/',
            {'type': 'start-session', 'data': '{}'})
        student_id = response.data['data']['student_id']
        # start solving a task
        response = self.client.post(
            '/api/actions/',
            {'type': 'start-task', 'data': json.dumps({'task_id': 'one-step-forward'})})
        task_session_id = response.data['data']['task_session_id']
        # solve the task
        response = self.client.post(
            '/api/students/{pk}/run_program/'.format(pk=student_id),
            {
                'task-session-id': str(task_session_id),
                'correct': True,
                'program': '',
            }
        )
        # check response
        self.assertEqual(response.data['correct'], True)
        self.assertIsNotNone(response.data['progress'])
        self.assertNotEqual(response.data['recommendation'], 'one-step-forward')
