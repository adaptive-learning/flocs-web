import json
from django.core.urlresolvers import reverse
from django.core.management import call_command
from django.test import TestCase

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


def get_recommendation(client):
    response = client.get(reverse('practice_recommend'))
    recommendation = json.loads(response.content.decode('utf-8'))
    return recommendation


def start_task(client, task_id):
    start_task_url = reverse('practice_start_task', kwargs={'task_id': task_id})
    client.post(start_task_url)
