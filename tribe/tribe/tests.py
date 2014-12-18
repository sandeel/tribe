from django.test import TestCase
from django.contrib.auth.models import User

class LoginTests(TestCase):

    def test_access_mytribe_without_being_logged_in_redirects_to_login(self):
        response = self.client.get('/mytribe/')

        self.assertRedirects(response, expected_url='/accounts/login/?next=/mytribe/', status_code=302, target_status_code=200, msg_prefix='')

from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class AccountTests(APITestCase):
    def setUp(self):
        self.client = AdminClient()
        self.user = User.objects.create_superuser(
            username='admin', email=None, password='123123')

    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('user-list')
        print(url)
        data = {'name': 'test_account', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)
