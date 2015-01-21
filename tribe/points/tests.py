from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from tribe.models import Tribe
from tribe.models import TribeUser
from rest_framework import status

# API Tests
class CategoryTests(APITestCase):


    def test_create_category_via_api_when_logged_in(self):
        """
        Ensure we can create a new category object via API
        """
        url = reverse('category-list')
        data = {
                    "name": "New Category Created For Test", 
                }
        tribe = Tribe(name="A New Test Tribe")
        tribe.save()
        user = TribeUser.objects.create(email="tester@test.com", password="password")
        user.tribe = tribe
        user.save()
        
        tribe.save()
        self.client.login(email='tester@test.com', password='password')
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_create_category_via_api_when_not_logged_in(self):
        """
        Ensure creating a Category object fails if not logged in
        """
        url = reverse('category-list')
        data = {
                    "name": "New Category Created For Test", 
                }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
