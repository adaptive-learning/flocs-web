from django.test import TestCase
from lazysignup.models import LazyUser
from lazysignup.utils import is_lazy_user
from users.services import create_or_convert


class UserTests(TestCase):
    def test_create_or_convert(self):
        user, username = LazyUser.objects.create_lazy_user()
        email = 'a@b.cz'
        first_name = 'Petr'
        password = '1234'
        converted_user = create_or_convert(user, email, first_name, password)

        self.assertEqual(user, converted_user)
        self.assertFalse(is_lazy_user(user))
        self.assertEqual(user.email, email)
        self.assertEqual(user.username, email)
        self.assertTrue(user.check_password(password))
        self.assertEqual(user.first_name, first_name)
