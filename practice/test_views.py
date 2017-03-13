import json
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.management import call_command
from django.test import TestCase
from practice.models import Student

class PracticeViewsTests(TestCase):

    def setUp(self):
        call_command('load_static_data')
            # TODO: is it possible to avoid the necessity of calling this command
            # for each test?

    def test_recommendation_view(self):
        """Recommendation should not change if the current task was not solved

        GET /api/practice/recommend/
        POST /api/practice/start_task/one-step-forward/
        GET /api/practice/recommend/
        """
        first_recommendation = get_recommendation(self.client)
        start_task(self.client, task_id=first_recommendation['task_id'])
        next_recommendation = get_recommendation(self.client)
        self.assertEqual(first_recommendation, next_recommendation)

    def test_see_instruction(self):
        """
        create student, see instruction, check student.see_instructions
        """
        user = User.objects.create()
        student = Student.objects.create(user=user)
        self.client.post(
            reverse('practice_see_instruction'),
            {'student_id': student.pk, 'instruction_id': 'block.shoot'})
        seen_instruction_ids = list(instruction.instruction_id
                                    for instruction in student.seen_instructions.all())
        self.assertEqual(seen_instruction_ids, ['block.shoot'])


def get_recommendation(client):
    response = client.get(reverse('practice_recommend'))
    recommendation = json.loads(response.content.decode('utf-8'))
    return recommendation


def start_task(client, task_id):
    start_task_url = reverse('practice_start_task', kwargs={'task_id': task_id})
    client.post(start_task_url)
