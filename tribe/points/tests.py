from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from tribe.models import Tribe
from tribe.models import TribeUser
from points.models import Task
from points.models import CheckIn
from points.models import Approval
from points.models import Category
from rest_framework import status
from django.utils import timezone

class TaskTests(TestCase):

    def setUp(self):
        self.tribe = Tribe(
                        name="The Testers",
                     )
        self.tribe.save()
        self.category = Category(
                                name="Household",
                                description="Around the house",
                                tribe=self.tribe
                                )
        self.category.save()

        self.user = TribeUser.objects.create(email="user@tests.com",password="password",)
        self.user.save()

        self.data = {
                    "name": "Test task",
                    "description": "Task created by unit test",
                    "category": self.category.id,
                    "points_reward": 1000,
                    "assigned_users": [self.user.id,],
                    "date_available": "",
                    "time_available_from": "",
                    "time_available_to": "",
                    "monday": False,
                    "tuesday": False,
                    "wednesday": False,
                    "thursday": False,
                    "friday": False,
                    "saturday": False,
                    "sunday": False,
                }

    def test_check_if_available_by_date(self):

        todays_date = timezone.now().date()
        task = Task()

        assert(not task.checkIfAvailable(todays_date))

        task.date_available=todays_date
        assert(task.checkIfAvailable(todays_date))

    def test_check_if_available_by_day_of_week(self):
        
        todays_date = timezone.now().date()

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

    def test_has_been_checked_in_on(self):
        task = Task(points_reward=1000, category=self.category)
        task.save()
        assert(not task.has_been_checked_in_on)

        checkin = CheckIn(task=task,
                          user=self.user,
                          date=timezone.now(),
                          points_awarded=1000)
        checkin.save()
        assert(task.has_been_checked_in_on)
        
    def test_create_task_via_api(self):
        """
        Ensure we can create a new task object via API
        """
        url = reverse('task-list')
        self.client.login(email=self.user.email, password='password')
        response = self.client.post(url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        """
        Ensure redirects to login when not authenticated
        """
        self.client.logout()
        response = self.client.post(url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_task_create_via_form(self):
        """
        Ensure we can create a new task object via form
        """
        url = reverse('task-create')
        


        """
        Ensure forbidden when not authenticated
        """
        self.client.logout()
        response = self.client.post(url, self.data, format="json")
        self.assertRedirects(response, "/accounts/login/?next=/mytribe/tasks/new/", status_code=302, target_status_code=200, msg_prefix='')


class CheckInTests(TestCase):

    def setUp(self):
        self.tribe = Tribe(
                        name="The Testers",
                     )
        self.tribe.save()
        self.category = Category(
                                name="Household",
                                description="Around the house",
                                tribe=self.tribe
                                )
        self.category.save()

        self.user = TribeUser(email="user@tests.com")
        self.user.save()

    def test_has_been_approved(self):
        task = Task(points_reward=1000, category=self.category)
        task.save()

        checkin = CheckIn(task=task,
                          user=self.user,
                          date=timezone.now(),
                          points_awarded=1000)
        checkin.save()
        assert(not checkin.has_been_approved)

        approval = Approval(approver=self.user)
        approval.save()
        checkin.approval = approval
        checkin.save()
        assert(checkin.has_been_approved)
        

        
class CategoryTests(TestCase):


    def test_create_category_via_api_when_authenticated(self):
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


    def test_create_category_via_api_when_not_authenticated(self):
        """
        Ensure creating a Category object fails if not logged in
        """
        url = reverse('category-list')
        data = {
                    "name": "New Category Created For Test", 
                }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

