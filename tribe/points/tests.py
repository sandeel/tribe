from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from tribe.models import Tribe
from tribe.models import TribeUser
from points.models import Task
from rest_framework import status
import datetime

class TaskTests(TestCase):

    def test_check_if_available_by_date(self):

        todays_date = datetime.datetime.today().date()
        task = Task()

        assert(not task.checkIfAvailable(todays_date))

        task.date_available=todays_date
        assert(task.checkIfAvailable(todays_date))

    def test_check_if_available_by_day_of_week(self):
        
        todays_date = datetime.datetime.today()

        task = Task()

        assert(not task.checkIfAvailable(todays_date))

        task.monday=True
        task.tuesday=True
        task.wednesday=True
        task.thursday=True
        task.friday=True
        task.saturday=True
        task.sunday=True

        assert(task.checkIfAvailable(todays_date))
        

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

