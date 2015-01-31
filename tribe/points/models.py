from tribe.models import Tribe
from tribe.models import TribeUser
import datetime
from django.db import models



class Category(models.Model):
    
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    tribe = models.ForeignKey(Tribe, related_name="categories")

class Task(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category)
    tribe = models.ForeignKey(Tribe, related_name="tasks", null=True)
    description = models.CharField(max_length=200)
    points_reward = models.IntegerField()
    assigned_users = models.ManyToManyField(TribeUser, related_name="tasks")

    #Available days
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    sunday = models.BooleanField(default=False)

    #Available from/to
    time_available_from = models.TimeField(null=True, blank=True)
    time_available_to = models.TimeField(null=True, blank=True)

    #Available date
    date_available = models.DateField(null=True, blank=True)

    @property
    def available_now(self):
        return self.checkIfAvailable(datetime.datetime.today())

    def checkIfAvailable(self,date):

        if CheckIn.objects.filter(task=self):
            return False

        if self.date_available:
            if self.date_available != date:
                return False
            ## check time
            return True

        # below happens if no date_available set

        day_of_week_of_date=date.weekday()
        print("date:",day_of_week_of_date)
        
        days = {
            0: self.monday,
            1: self.tuesday,
            2: self.wednesday,
            3: self.thursday,
            4: self.friday,
            5: self.saturday,
            6: self.sunday,
        }

        if days[day_of_week_of_date] == True:
            return True

        return False

class CheckIn(models.Model):
    user = models.ForeignKey(TribeUser, related_name="checkins")
    task = models.ForeignKey(Task, related_name="checkins")
    date = models.DateTimeField()
    points_awarded = models.IntegerField()
