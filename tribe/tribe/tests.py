from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from tribe.models import Tribe
from tribe.models import TribeUser
from tribe.models import InvitedUser

class AccountTests(APITestCase):

    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('tribeuser-list')
        data = {'email': 'tester@test.com', 'password': 'password'}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_tribe(self):
        """
        Ensure we can create a new tribe object
        """
        url = reverse('tribe-list')
        data = {
                    "name": "New Tribe", 
                    "invited_users": [], 
                    "members": [], 
                    "leaders": []
                }
        user = TribeUser.objects.create(email="tester@test.com", password="password")
        user.save()
        self.client.login(email='tester@test.com', password='password')
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invited_user_gets_added_to_correct_tribe(self):
        tribe = Tribe(name="Celtic Tribe")
        tribe.save()
        invited_user = InvitedUser(email="dwight@schrute.com",tribe=tribe)
        invited_user.save()
        user = TribeUser.objects.create(email="dwight@schrute.com",password="password")
        user.save()
        self.assertEqual(user.tribe.pk, tribe.pk)
