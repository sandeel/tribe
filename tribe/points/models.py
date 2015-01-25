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
    tribe = models.ForeignKey(Tribe, related_name="task_templates", null=True)
    description = models.CharField(max_length=200)
    recurring_strategy = models.CharField(max_length=200)
    points_reward = models.IntegerField()
    assigned_users = models.ManyToManyField(TribeUser, related_name="task_templates")
