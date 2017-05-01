from django.contrib.auth import login
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.test import Client, TestCase, RequestFactory
from lazysignup.utils import is_lazy_user
from lazysignup.models import LazyUser
import pytest
from social_django.utils import load_strategy, load_backend


def do_authenticate(user=None, next_uri='/api/users/'):
    facebook_state = 'ABC'
    client = Client()
    session = client.session
    session['facebook_state'] = facebook_state
    session['next'] = next_uri
    session.save()
    request_factory = RequestFactory()
    request = request_factory.get(path='/social/complete/facebook/',
                                  data={
                                      'redirect_state': 'DEF',
                                      'granted_scopes': 'email,public_profile',
                                      'denied_scopes': '',
                                      'code': 'GHI',
                                      'state': facebook_state,
                                  })
    request.user = user if user else AnonymousUser()
    request.session = session
    request.session = client.session
    request.social_strategy = load_strategy(request)
    request.strategy = request.social_strategy
    backend = load_backend(request.strategy, 'facebook', '/social/complete/facebook/')
    request.backend = backend

    args = ()
    kwargs = {
        'backend': backend,
        'response': {'name': 'Pepa Novák', 'id': '1234', 'expires': 1000,
                     'granted_scopes': ['email', 'public_profile'], 'access_token': 'A'},
        'user': user,
    }

    return backend.strategy.authenticate(*args, **kwargs), request.session.get('next')


class PipelineTest(TestCase):
    logged_in_user = None
    logged_out_user = None

    def record_user_logged_in(self, sender, user, request, **kwargs):
        self.logged_in_user = user

    def record_user_logged_out(self, sender, user, request, **kwargs):
        self.logged_out_user = user

    @pytest.mark.django_db
    def test_no_user(self):
        user, _ = do_authenticate()
        self.assertIsNotNone(user, 'Processed user should not have been None.')
        social_users = user.social_auth.all()
        self.assertNotEqual(social_users, [], 'No social auth user has been created.')

    @pytest.mark.django_db
    def test_convert_lazy_user(self):
        lazy_user, _ = LazyUser.objects.create_lazy_user()
        user, _ = do_authenticate(lazy_user)
        self.assertFalse(is_lazy_user(lazy_user), 'Lazy user should have been converted.')
        lazy_user = User.objects.get(pk=lazy_user.pk)  # refresh original user object
        self.assertIsNotNone(user, 'Processed user should not have been None.')
        self.assertEqual(user, lazy_user, 'No new user should have been created.')
        social_users = user.social_auth.all()
        self.assertNotEqual(social_users, [], 'No social auth user has been created.')

    @pytest.mark.django_db
    def test_associate_user(self):
        original_user = User(username='Karel')
        original_user.save()
        user, _ = do_authenticate(original_user)
        original_user = User.objects.get(pk=original_user.pk)  # refresh original user object
        self.assertIsNotNone(user, 'Processed user should not have been None.')
        self.assertEqual(user, original_user, 'No new user should have been created.')
        social_users = user.social_auth.all()
        self.assertNotEqual(social_users, [], 'No social auth user has been created.')

    @pytest.mark.django_db
    def test_logout_user(self):
        user_logged_in.connect(self.record_user_logged_in)
        user_logged_out.connect(self.record_user_logged_out)

        user, _ = do_authenticate()

        new_user = User(username='Karel')
        new_user.backend = 'django.contrib.auth.backends.ModelBackend'
        new_user.save()

        request = RequestFactory().get('/')
        request.session = Client().session
        login(request, new_user)

        user2, _ = do_authenticate(new_user)

        self.assertIsNotNone(user, 'Processed user should not have been None.')
        self.assertEqual(user, user2, 'No new user should have been created.')
        self.assertNotEqual(self.logged_in_user, new_user, 'Second user should have been logged out.')
        self.assertEqual(self.logged_out_user, new_user, 'Second user should have been logged out.')
        self.assertEqual(self.logged_in_user, user, 'First user should have been logged out.')
        self.assertNotEqual(self.logged_out_user, user, 'First user should have been logged out.')

    def test_keep_next_redirect(self):
        next_uri = '/test/'
        _, next_returned = do_authenticate(next_uri=next_uri)
        self.assertEqual(next_returned, next_uri, 'Redirect using next parameter has not been retained.')

        new_user = User(username='Karel')
        new_user.backend = 'django.contrib.auth.backends.ModelBackend'
        new_user.save()

        request = RequestFactory().get('/')
        request.session = Client().session
        login(request, new_user)

        _, next_returned = do_authenticate(new_user, next_uri=next_uri)
        self.assertEqual(next_returned, next_uri, 'Redirect using next parameter has not been retained.')
