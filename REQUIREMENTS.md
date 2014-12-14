Requirement Specification: Tribe
================================

# Overview

Tribe is an application for efficient families.

Each member of the family uses Tribe. Family members complete daily tasks to earn points which unlock rewards. Achievements can also be unlocked by users which earn more points.

## The Problem
* Kids need motivation to do homework and do tasks like cleaning their bedrooms
* Families are busy and find it hard to keep track of what other family members are doing and when
* Family members spend their days in different locations

## Aims of Tribe

**Motivation**
Create motivation for family members to work together on completing day-to-day tasks.

**Schoolwork**
Remind and encourage kids to complete homework.

**Accountability**
Allow parents to check that kids' homework has been done. Make sure everybody knows the dog has already been walked and fed.

**Family Interaction**
Encourage the family to spend time together and co-operate.

**Fun**
Give a sense of satisfaction and joint achievement and add a fun element to day-to-day tasks.

# How it works

Each member of the family who is signed up to Tribe becomes a "tribe member".

A parent, (or both parents, or even an older child or child minder) becomes the "tribe leader".

## Tasks

Tribe leaders create tasks.

Tasks can be once-off or recurring, eg. daily tasks ("do homework") or weekly tasks ("take out bins").

Tribe members complete tasks, and mark them as "done" using either the web interface or mobile app. Optionally a photo can be uploaded as proof that the task has been completed.


## Points

A Tribe Leader confirms that the task has been done and the points are awarded to the Tribe as a whole.

The accumulated points are visible to all tribe members.


## Rewards

If the tribe scores enough points in a given week, rewards are unlocked. Rewards are in "levels" eg., the Level 1 rewards might be unlocked after 100 points, Level 2 after 200, and so on.

Rewards are set by a tribe leader, and are specific to tribe members. For example, for parents the Level 1 reward might be a bottle of wine or cinema trip. For the older kids, the equivalent reward might be pocket money or phone top-up. For the youngest kid, it might be sweets. It is up to the tribe leader to ensure the rewards are roughly equal in value. All tribe members can view what rewards (for both themselves and other tribe members) are available for each level on a given week.

Tribe has a selection of default rewards to choose from, however the Tribe leaders have the option to customise the rewards.

Sample rewards for kids are

* amounts of pocket money (a multiplier system is available to award appropriate levels of pocket money based on the kids' ages)
* phone top-up credit
* presents (eg. a toy, new phone)


### Achievements
Extra points can be earned when a family member earns an achievement.

An achievement something remarkable that a tribe member did, such as completing a task x number of days in a row, completing a large number of tasks in a small space of time, and so on.

Tribe leaders create achievements but there are some defaults already created.

Achievements can be won more than once by the same person.

Gaining an achievement puts a badge on the tribe member's profile page.


### Categories
Tasks can fit into a category.

Information about how many points have been scored in a certain category are available, giving the Tribe an idea of where they are doing well and where improvements are needed.

Tribe provides several categories by default:

* Household
* Diet
* Fitness
* Pets
* Learning and School



# User Stories


## Roles

### Tribe Leader
This is usually a parent.

### Tribe Member
Any member of the family.


***


**As a new user I want to sign up to Tribe because I want to get my family to do some work.**

The user enters

* email
* family name
* password


***


**As a tribe leader I want to add my family members to the tribe because I want to have my whole family set up using Tribe**

Data entered

* name
* email
* password


***


**As a tribe member I want to sign in so I can use features of Tribe**

User needs to enter

* email
* password


***


**As a tribe member I want to edit my profile because I want to add details about myself and choose a picture.**

* name
* picture (upload or choose an icon)


***


**As a tribe leader I want to add a task because I have thought of a new task that needs doing.**

The tribe leader enters

* task name
* description
* task category
* location
* recurring strategy (including once-off)
* number of points rewarded for completing the task


***


**As a tribe leader I want to edit a task which has already been created because an element of the task has changed or was entered incorrectly.**

All elements of a task are editable via a form.


***


**As a tribe leader I want to delete a task because I've decided this task should no longer be in the system or it doesn't need doing anymore.**

The user should be asked to confirm they want to delete the task completely.


***


**As a tribe member I want to see the number of points my tribe has accumulated this week because I want to see how close we are to winning a reward.**

The points are displayed on a graph showing how close tribe is to the next reward and what the reward is for each family member.


***


**As a tribe member I want to see a graph of how many points the tribe has accumulated on a per-week and category basis so far because I want to see if we are making and improvement or disprovement**

Points are displayed on a graph showing weekly totals. Task categories can be toggled on and off.


***


**As a tribe leader I want to create, edit or delete a reward which can be won by tribe members because I want to select this as a reward for a tribe member at a points level**

Details entered are

* Reward name
* Icon image (upload or select from a selection)
* Optional description


***


**As a tribe leader I want to set the rewards for a given week for each level because I want to decide what each tribe member will receive when the points are acieved.**

The rewards for each tribe member at a specific level are entered.


***


**As a tribe member I want to mark a task as done because I have completed a task and want to earn points for it.**

This means the task has been done in real life and is ready for checking by a tribe leader.


***


**As a tribe leader I want to create a new task category or edit existing categories because I want points to control how points are tracked.**

* Category name
* Optional description
* Colour
* Icon (upload or select)


***


**As a tribe member I want to view the current rewards levels because I want to see how many points are needed for each.**


***


**As a tribe leader I want to edit the current reward levels so that they are appropriate to the level of points the family can earn.**

Each level required points are editable.


***


**As a tribe leader I want to create or edit an achievement to encourage the family to win more points.**

Data entered:

* Achievement name
* Task(s) related to the achievement
* Pattern required to achieve (eg. "10 in a row")
* Points awarded when this achievement is earned


***


**As a tribe member I want to view my or another tribe member's profile because I want to see how they are doing and see what achievements they have gained**

Profile page shows

* Tribe member's name
* Stats on points and tasks
* Achievements gained


***


**As a tribe leader I want to see what rewards are owed to a tribe member in real life and mark them as complete once they have been awarded in real life**

The rewards which are owed to which tribe member are visible and marked as pending or complete (meaning the reward has been physically given to the tribe member).
