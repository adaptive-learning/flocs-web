import json
from django.core.management import call_command
from django.test import TestCase

class FlocsWebViewsTests(TestCase):

    def setUp(self):
        call_command('load_static_data')
            # TODO: is it possible to avoid the necessity of calling this command
            # for each test? (maybe create a fixture in advance and only
            # specify the fixture)

    def test_start_session(self):
        """ Anonymous user should be able to start session and obtain student_id
        """
        response = decode(self.client.post(
            '/api/actions/',
            {'type': 'start-session', 'data': '{}'}
        ))
        self.assertIsNotNone(response['action_id'])
        self.assertEqual(response['type'], 'start-session')
        # NOTE: the following line is a hack to overcome bad json fields handling
        # (TODO: which should be solved asap)
        data = json.loads(response['data'].replace("'", '"'))
        self.assertIsInstance(data, dict)
        self.assertIsNotNone(data['student_id'])
        self.assertIsNotNone(data['session_id'])
        # start session again -> should return the same user and even the session
        response2 = decode(self.client.post(
            '/api/actions/',
            {'type': 'start-session', 'data': '{}'}
        ))
        data2 = json.loads(response2['data'].replace("'", '"'))
        self.assertEqual(response2['type'], 'start-session')
        self.assertEqual(data2['student_id'], data['student_id'])
        self.assertEqual(data2['session_id'], data['session_id'])


def decode(response):
    return json.loads(response.content.decode('utf-8'))
