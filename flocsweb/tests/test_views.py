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
        # TODO: do the test properly, there are currently some simplifying
        # hacks to overcome the issue with bad jsonfields handling
        response = self.client.post(
            '/api/actions/',
            {'type': 'start-session', 'data': '{}'}
        )
        self.assertIsNotNone(response.data['action_id'])
        self.assertEqual(response.data['type'], 'start-session')
        self.assertIn('student_id', response.data['data'])
        self.assertIn('session_id', response.data['data'])
        # start session again -> should return the same user and even the session
        #print(response.data)
        #print(response.content)
        response2 = self.client.post(
            '/api/actions/',
            {'type': 'start-session', 'data': '{}'}
        )
        self.assertEqual(response2.data['type'], 'start-session')
        #self.assertEqual(response2.data['data'], response.data['data'])
