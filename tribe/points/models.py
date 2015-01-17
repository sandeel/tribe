from django.db import models
from tribe.models import Tribe
from tribe.models import TribeUser

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
    assigned_users = models.ManyToManyField(TribeUser, related_name="task_templates")

    def save(self, *args, **kwargs):
        super(TaskTemplate, self).save(*args, **kwargs)

        task = Task(task_template = self)
        task.save()

class Task(models.Model):
    def __str__(self):
        return self.task_template.name

    task_template = models.ForeignKey(TaskTemplate,null=False)
    marked_done = models.BooleanField(default=False)

