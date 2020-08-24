from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        email = 'test@gmail.com'
        password = '1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEquals(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        email = 'test@GMAIL.com'
        user = get_user_model().objects.create_user(email, '1234')

        self.assertEquals(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('       ', '12334')

    def test_create_new_super_user(self):
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'abcdef'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
