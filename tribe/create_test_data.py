#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import django
import os

os.environ['DJANGO_SETTINGS_MODULE'] = "tribe.settings"

django.setup()

import os
import json
from tribe.models import Tribe
from tribe.models import TribeUser
from points.models import Task
from points.models import Category
from points.models import Reward
from faker import Factory
import random

# create a fake data generator
fake = Factory.create()

#Clear the database
os.system( "python manage.py flush" )

"""
Generate a fake one-word name
"""
def getNewName():
    
    name = fake.name().split()[0]
    while any(title in name for title in ('.', 'Miss', 'Dr')):
        name = fake.name().split()[0]
    
    return name


"""
Create a tribe and tribe members
"""

## Create a fake name for the tribe
## get a random three word sentence and strip the full stop
name = fake.sentence(nb_words=1)[:-1]+str(random.randint(0,1000))
tribe = Tribe.objects.create(name=name)

dad = TribeUser.objects.create(email=fake.email(), password="password", name=getNewName())
dad.add_to_tribe(tribe)

mam = TribeUser.objects.create(email=fake.email(), password="password", name=getNewName())
mam.add_to_tribe(tribe)

kid1 = TribeUser.objects.create(email=fake.email(), password="password", name=getNewName())
kid1.add_to_tribe(tribe)

kid2 = TribeUser.objects.create(email=fake.email(), password="password", name=getNewName())
kid2.add_to_tribe(tribe)

kid3 = TribeUser.objects.create(email=fake.email(), password="password", name=getNewName())
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
    points_reward = 20, 
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
    points_reward = 40, 
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
    points_reward = 15, 
    monday = True, 
    tuesday = True,
    wednesday = True,
    thursday = True,
    friday = True,
    saturday = True,
    sunday = True,
)
task3.assigned_users.add(dad, mam, kid1, kid2, kid3)

task4 = Task.objects.create(
    tribe = tribe,
    name = "Feed the dogs.",
    description = "One can of pedigree chum each.", 
    category = Category.objects.get(tribe=tribe, name="Pets"),
    points_reward = 15, 
    monday = True, 
    tuesday = True,
    wednesday = True,
    thursday = True,
    friday = True,
    saturday = True,
    sunday = True,
)
task4.assigned_users.add(dad, mam, kid1, kid2, kid3)

task6 = Task.objects.create(
    tribe = tribe,
    name = "Make bed.",
    description = "Make own bed.", 
    category = Category.objects.get(tribe=tribe, name="Household"),
    points_reward = 5, 
    monday = True, 
    tuesday = True,
    wednesday = True,
    thursday = True,
    friday = True,
    saturday = True,
    sunday = True,
)
task6.assigned_users.add(dad, mam, kid1, kid2, kid3)

task7 = Task.objects.create(
    tribe = tribe,
    name = "Tidy bedroom.",
    description = "Take everything off floor, dirty clothes in laundry basket.", 
    category = Category.objects.get(tribe=tribe, name="Household"),
    points_reward = 10, 
    monday = True, 
    tuesday = True,
    wednesday = True,
    thursday = True,
    friday = True,
    saturday = True,
    sunday = True,
)
task7.assigned_users.add(dad, mam, kid1, kid2, kid3)

task8 = Task.objects.create(
    tribe = tribe,
    name = "Brush teeth",
    description = "Brush teeth with toothpaste in bathroom.",
    category = Category.objects.get(tribe=tribe, name="Household"),
    points_reward = 5, 
    monday = True, 
    tuesday = True,
    wednesday = True,
    thursday = True,
    friday = True,
    saturday = True,
    sunday = True,
)
task8.assigned_users.add(dad, mam, kid1, kid2, kid3)


task9 = Task.objects.create(
    tribe = tribe,
    name = "Do homework",
    description = "Every subject. Check homework journal.",
    category = Category.objects.get(tribe=tribe, name="School"),
    points_reward = 30, 
    monday = True, 
    tuesday = True,
    wednesday = True,
    thursday = True,
    friday = True,
    saturday = True,
    sunday = True,
)
task9.assigned_users.add(kid1, kid2, kid3)


# generate rewards for the tribe

reward = Reward.objects.create(name = "€5 pocket money",
                               description="Cash",
                               points_required=50,
                               tribe = tribe)
reward.available_to.add(dad,mam,kid1,kid2,kid3)

reward = Reward.objects.create(name = "€10 pocket money",
                               description="Cash",
                               points_required=100,
                               tribe = tribe)
reward.available_to.add(dad,mam,kid1,kid2,kid3)

reward = Reward.objects.create(name = "Two hours of PlayStation",
                               description="Taken all in one go",
                               points_required=200,
                               tribe = tribe)
reward.available_to.add(dad,mam,kid1,kid2,kid3)

reward = Reward.objects.create(name = "Take-away",
                               description="",
                               points_required=300,
                               tribe = tribe)
reward.available_to.add(dad,mam,kid1,kid2,kid3)

reward = Reward.objects.create(name = "Bottle of wine",
                               description="",
                               points_required=150,
                               tribe = tribe)
reward.available_to.add(dad,mam,kid1,kid2,kid3)

num_rewards = 5

for x in range(0,num_rewards):

    points_required = (10*(random.randint(1,50)))
    reward = Reward.objects.create(name = fake.sentence(nb_words=3),
                                   description = fake.sentence(),
                                   points_required=points_required,
                                   tribe = tribe)
    reward.available_to.add(dad,mam,kid1,kid2,kid3)

print("Login: ", dad.email)
