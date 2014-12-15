# Entities

## TribeMember
* user
* name
* picture
* tasksCompleted

## TaskTemplate
* name
* description
* category
* recurring strategy
* location
* number of points rewarded
* active

## Task
* taskTemplate
* dueDate
* completedByPerson (null if not completed)
* completedTime (null if not completed)
* value

## Reward
* name
* image
* description

## LevelTier
* value
* description
* rewardsForEachMember

## RewardsOwed
* user
* reward
* dateReceived
* dateCreated

## Location
* name
* co-ords

## Achievement
* name
* description
* icon
* pattern
* value

## Category
* name
* description
* colour
* icon


