from django.db import models
from tribe.models import Tribe

class Category(models.Model):
    
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    tribe = models.ForeignKey(Tribe, related_name="categories")

class TaskTemplate(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category)
    tribe = models.ForeignKey(Tribe, related_name="task_templates")
    description = models.CharField(max_length=200)
    recurring_strategy = models.CharField(max_length=200)
    points_reward = models.IntegerField()
