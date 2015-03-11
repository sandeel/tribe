# Diary

## 2014-12-08
* Came up with a name for the application: tribe
* Created the git repo locally and on Github
* Signed up to Taiga.io
* Created a project for tribe on Taiga.io
* Created some user stories on Taiga


## 2014-12-12
Created a powerpoint for the mid point presentation 
Put together a very rough demo of the application using Django


## 2014-12-13
Presented the idea and received feedback from Eamonn


## 2014-12-14
Worked on the requirement spec
Submitted the requirement spec on Moodle
Emailed Mikhail requirement spec requesting feedback
Started putting all user stories into Taiga
started creating a text file with all my entities
worked more on the entities


## 2014-12-16
coding


## 2014-12-17
Coding
researching Django REST Framework


## 2014-12-18

* started tutorial for Django Rest Framework. Completed [this section](http://www.django-rest-framework.org/tutorial/1-serialization/)
* discovered [httpie](https://github.com/jakubroztocil/httpie)

# Sprint 1

## 2014-12-28

* mapped out 10 sprints on taiga.io leading up to project completion date
* 

## 2014-12-29
* continued tutorial on Django Rest Framework
* updated some project documentation

## 2014-12-30
* continued tutorial on Django Rest Framework
* Discovered [MkDocs](http://www.mkdocs.org/), which I may use for the documentation of the project
* [This page](http://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/) of DRF tutorial will be useful for user API auth
* completed tutorial on DRF


## 2014-12-31
* Several hours working on permissions in the Django Rest Framework
* Created permission for allowing unregistered users to create a new user (eg. register via mobile app)


## 2015-01-01
* Almost completed sign up by API

## 2015-01-02
* Completed sign up via API and also implemented creating a tribe via the API

## 2015-01-04
* Started to implement inviting new users.


## 2015-01-10
* Working for few hours on adding new users to your tribe via the edit tribe page. Almost ready for test.
* uploaded December diary to Moodle


## 2015-01-11
* Finished form for adding a new tribe member to your tribe
* Wrote unit test for above functionality




# Sprint 2 (12th Jan 2015 - 25th Jan 2015)


## 2015-01-12
* Added models for TaskTemplates and Categories.
* Added a view for viewing Task templates


## 2015-01-14
* Working on the models/database tables for TaskTemplates
* Form for new TaskTemplate

## 2015-01-14
* Forms for editing TaskTemplates and viewing details.


## 2015-01-20
* Added models, forms, views etc. for Categories
* Added some more user stories to [Taiga.io](https://www.taiga.io) project
* Got most of the user stories laid out in sprints in Taiga.io

## 2015-01-21
* Created a serializer for Categories
* Created API endpoint for creating and viewing categories
* Wrote tests for creating Categories via API


## 2015-01-22
* Created a serializer for Task
* Created API endpoints for task.
* Need to write tests for this next


## 2015-01-25
* Today I started refactoring the code so that the forms use the app's own API



# Sprint 3 (26th Jan 2015 - 08th Feb 2015)

## 2015-01-26
* Created CheckIn class. There will now be no TaskTemplate, instead the Task will be a monolithic object which has available times and a CheckIn will refer to an instance of marking a task as done. This is to give more flexibility to different types of tasks eg. family dinners.


## 2015-01-28
* Added a "Check In" button to tasks which creates an instance of a check in for a user on that task and awards points. This uses the API in the background.


## 2015-01-31
* Created an approvals system for tribe leaders to approve tasks
* Started working on some test data

## 2015-02-01
* Wrote lots of tests today

## 2015-02-02
* wrote more tests
* Investigating and reading about Apache Cordova
* Started working on the mobile app.
* Using ngrok to publicly host the site for the app to communicate with.


## 2015-02-03
* Working more on the mobile app and working on styling to ensure site looks ok on both mobile and desktop
* Added basic points calculation for users (done by counting up the points awarded for each checkin which has been approved)

## 2015-02-04
* Redesigned home page and user interface (prototype design for finished product). Started CSS style sheet for site.
* Changed permissions for some views eg. Task list.


## 2015-02-05
* Investigated continuous integration service Travis CI.
* Created account with travis and config file to tell it how to test my code
* Builds passing. Added small button to my project's github page to indicated if builds are passing or not.
* Added a collapsible navigation sidebar to the site. Ensured it also works on mobile


# Sprint 4 "Points"
## 10th February - 22nd February 2015


## 2015-02-17
* Created calculation methods for total points for a Tribe. (still need to write
tests for these)
* Created a display for these points on a per-day basis on the points page


# Sprint 5 "Rewards"

## 2015-02-24
* Created a model for a reward
* Created serializer for a reward
* Created views for adding rewards

## 2015-02-26
* Created views for editing rewards
* Researching drawing graphs in HTML5
* Researching the native Progress element in HTML5
* Added a basic progress bar for weekly points using bootstrap for the styles

#2015-03-10
* Revamped the UI
