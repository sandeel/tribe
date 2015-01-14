# Entities

## Tribe
* name
* owner
* tribeLeaders
* tribeMembers


***


## TribeMember
* user
* tribe
* name
* picture
* tasksCompleted


***


## TaskTemplate
* tribe
* name
* description
* category
* recurring strategy
* location
* number of points rewarded


***


## Task
* tribe
* taskTemplate
* dueDate
* completedByPerson (null if not completed)
* completedTime (null if not completed)
* value


***


## PointsBatch

Arbitrary number of points given to a user at a specific datetime

* pointsValue
* datetime


***


## Reward
* tribe
* name
* image
* description


***


## LevelTier
* tribe
* value
* description
* rewardsForEachMember


***


## RewardsOwed
* tribe
* user
* reward
* dateReceived
* dateCreated


***


## Location
* tribe
* name
* co-ords


***


## Achievement
* tribe
* name
* description
* icon
* pattern
* value


***


## Category
* tribe
* name
* description
* colour
* icon


***
