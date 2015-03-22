from django.contrib import admin
from points.models import Category
from points.models import Task
from points.models import CheckIn
from points.models import Approval
from points.models import Reward


admin.site.register(Category)
admin.site.register(Task)
admin.site.register(CheckIn)
admin.site.register(Approval)
admin.site.register(Reward)
