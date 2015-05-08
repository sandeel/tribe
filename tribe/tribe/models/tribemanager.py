from django.db import models
import datetime
from points.models import Category

class TribeManager(models.Manager):

    def create(self, name="My Tribe"):

        tribe = self.model(
            name=name,
        )

        tribe.save()

        # create some default categories
        tribe.categories.create(tribe=tribe,
                                name="Household",
                                description="Jobs around the house.")
        tribe.categories.create(tribe=tribe,
                                name="Pets",
                                description="The animals of the house.")
        tribe.categories.create(tribe=tribe,
                                name="School",
                                description="School and homework.")
        tribe.categories.create(tribe=tribe,
                                name="Sports and fitness",
                                description="All sports",)
        tribe.categories.create(tribe=tribe,
                                name="Tribe",
                                description="Related to admin of the tribe",)

        # create some default tasks
        two_weeks_from_now = (datetime.datetime.today() + datetime.timedelta(days=14))

        tribe.tasks.create(
            tribe = tribe,
            name = "Invite your tribe",
            description = "Go to the tribe page and invite your tribe members \
                           by entering their email addresses",
            category = Category.objects.get(tribe=tribe, name="Tribe"),
            points_reward = 20, 
            date_available= datetime.datetime.today(),
            date_available_to = two_weeks_from_now,
        )

        tribe.tasks.create(
            tribe = tribe,
            name = "Profile photos",
            description = "Upload photos for each tribe member via their profile \
                           pages.",
            category = Category.objects.get(tribe=tribe, name="Tribe"),
            points_reward = 40, 
            date_available= datetime.datetime.today(),
            date_available_to = two_weeks_from_now,
        )

        tribe.tasks.create(
            tribe = tribe,
            name = "Approve check-in",
            description = "After checking in in a task, approve the check-in \
                           to score points.",
            category = Category.objects.get(tribe=tribe, name="Tribe"),
            points_reward = 60, 
            date_available= datetime.datetime.today(),
            date_available_to = two_weeks_from_now,
        )

        return tribe

