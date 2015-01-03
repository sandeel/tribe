from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

class AccountTests(APITestCase):

    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('tribeuser-list')
        data = {'email': 'tester@test.com', 'password': 'password'}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TribeTests(APITestCase):

    def test_create_tribe(self):
        """
        Ensure we can create a new tribe object
        """
        url = reverse('tribe-list')
        data = {'name': 'new tribe', 'members': ''}
        user = get_user_model().objects.create_user(email="tester@test.com", password="password")
        user.save()
        self.client.login(email='tester@test.com', password='password')
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


