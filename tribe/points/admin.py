from django.contrib import admin
from points.models import Category
from points.models import Task
from points.models import CheckIn

admin.site.register(Category)
admin.site.register(Task)
admin.site.register(CheckIn)
