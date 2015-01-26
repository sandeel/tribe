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




# Sprint 2


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


## 2015-01-26
* Created CheckIn class. There will now be no TaskTemplate, instead the Task will be a monolithic object which has available times and a CheckIn will refer to an instance of marking a task as done. This is to give more flexibility to different types of tasks eg. family dinners.
