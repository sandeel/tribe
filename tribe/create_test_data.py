"""
Tun this script,
export DJANGO_SETTINGS_MODULE=yoursite.settings
"""
import django
django.setup()

import os
import json

from tribe.models import Tribe
from tribe.models import TribeUser
from points.models import Task
from points.models import Category

"""
Clear the database
"""
os.system( "python manage.py flush" )

tribe = Tribe.objects.create(name="The Dinosaurs")

dad = TribeUser.objects.create("otis.redding@eircom.net", "password", name="Otis")
dad.add_to_tribe(tribe)

mam = TribeUser.objects.create("cjepsen@gmail.com", "password", name="Carly Rae")
mam.add_to_tribe(tribe)

kid1 = TribeUser.objects.create("alan@yahoo.com", "password", name="Al")
kid1.add_to_tribe(tribe)

kid2 = TribeUser.objects.create("pearse@yahoo.com", "password", name="Pearse")
kid2.add_to_tribe(tribe)

kid3 = TribeUser.objects.create("raymond@yahoo.com", "password", name="Ray")
kid3.add_to_tribe(tribe)

"""
make mam and dad leaders
"""
tribe.leaders.add(dad)
tribe.leaders.add(mam)

"""
Create some tasks
"""
task1 = Task.objects.create(
    tribe = tribe,
    name = "Take out the bins",
    description = "Put the green and black bins out on the road.", 
    category = Category.objects.get(tribe=tribe, name="Household"),
    points_reward = 10, 
    monday = True, 
    tuesday = False,
    wednesday = False,
    thursday = False,
    friday = False,
    saturday = False,
    sunday = True,
)
task1.assigned_users.add(dad, mam, kid1, kid2, kid3)

task2 = Task.objects.create(
    tribe = tribe,
    name = "Take the dogs for a walk.",
    description = "At least 15 mins.", 
    category = Category.objects.get(tribe=tribe, name="Pets"),
    points_reward = 10, 
    monday = True, 
    tuesday = True,
    wednesday = True,
    thursday = True,
    friday = True,
    saturday = True,
    sunday = True,
)
task2.assigned_users.add(dad, mam, kid1, kid2, kid3)

task3 = Task.objects.create(
    tribe = tribe,
    name = "Put on a laundry wash.",
    description = "Empty the linen baskets from all bedrooms.", 
    category = Category.objects.get(tribe=tribe, name="Household"),
    points_reward = 10, 
    monday = True, 
    tuesday = False,
    wednesday = False,
    thursday = False,
    friday = False,
    saturday = False,
    sunday = True,
)
task3.assigned_users.add(dad, mam, kid1, kid2, kid3)

task3 = Task.objects.create(
    tribe = tribe,
    name = "Put on a laundry wash.",
    description = "Empty the linen baskets from all bedrooms.", 
    category = Category.objects.get(tribe=tribe, name="Household"),
    points_reward = 10, 
    monday = True, 
    tuesday = False,
    wednesday = False,
    thursday = False,
    friday = False,
    saturday = False,
    sunday = True,
)
task3.assigned_users.add(dad, mam, kid1, kid2, kid3)
# laundry
# feed dogs
# make bed
# tidy bedroom
# do homework
# put away toys
# make dinner
# brush teeth
