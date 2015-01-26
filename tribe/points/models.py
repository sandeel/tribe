from django.db import models
from tribe.models import Tribe
from tribe.models import TribeUser

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
    time_available_from = models.TimeField()
    time_available_to = models.TimeField()

    #Available date
    date_available = models.DateField()
    

class CheckIn(models.Model):
    task = models.ForeignKey(Task, related_name="checkins")
    date = models.DateField()
    time = models.TimeField()


