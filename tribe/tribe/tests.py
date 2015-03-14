from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from tribe.models import Tribe
from tribe.models import TribeUser
from tribe.models import InvitedUser
import json

class AccountTests(APITestCase):

    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('tribeuser-list')
        data = {'email': 'tester@test.com', 'password': 'password', 'name': 'Test'}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        """
        Ensure that a tribe was created for the user with the correct name
        """
        url = reverse('tribe-list')
        self.client.login(email='tester@test.com', password='password')
        response = self.client.get(url,  {}, HTTP_X_REQUESTED='XMLHttpRequest')
        json_string = response.content.decode()
        data = json.loads(json_string)
        self.assertEqual(data["results"][0]["name"], "Test\'s tribe")
        


    def test_dont_allow_duplicate_emails(self):
        """
        Ensure new user can't use same email as a user which already
        exists
        """
        url = reverse('tribeuser-list')
        data1 = {'email': 'tester@test.com', 'password': 'password', 'name': 'Test1'}
        data2 = {'email': 'tester@test.com', 'password': 'password', 'name': 'Test2'}

        response1 = self.client.post(url, data1, format="json")
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)

        response2 = self.client.post(url, data2, format="json")
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)

    ### TEST MAKE SURE DON'T ALLOW DUPLICATE EMAILS

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

    def test_create_tribe_when_not_authenticated(self):
        url = reverse('tribe-list')
        data = {
                    "name": "New Tribe", 
                    "invited_users": [], 
                    "members": [], 
                    "leaders": []
                }
        user = TribeUser.objects.create(email="tester@test.com", password="password")
        user.save()
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        

    def test_invited_user_gets_added_to_correct_tribe(self):
        tribe = Tribe(name="Celtic Tribe")
        tribe.save()
        invited_user = InvitedUser(email="dwight@schrute.com",tribe=tribe)
        invited_user.save()
        user = TribeUser.objects.create(email="dwight@schrute.com",password="password")
        user.save()
        self.assertEqual(user.tribe.pk, tribe.pk)
