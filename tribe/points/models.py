import datetime
from django.db import models
import os



class Category(models.Model):
    
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    tribe = models.ForeignKey('tribe.Tribe', related_name="categories")


class Task(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category)
    tribe = models.ForeignKey('tribe.Tribe', related_name="tasks", null=True)
    description = models.CharField(max_length=200)
    points_reward = models.IntegerField()
    assigned_users = models.ManyToManyField(
                                        'tribe.TribeUser',
                                        related_name="tasks",
                                        )

    #Available days
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    sunday = models.BooleanField(default=False)

    #Available from/to
    time_available_from = models.TimeField(null=True, blank=True)
    time_available_to = models.TimeField(null=True, blank=True)

    #Available date
    date_available = models.DateField(null=True, blank=True)
    date_available_to = models.DateField(null=True, blank=True)

    @property
    def available_now(self):
        return self.checkIfAvailable(datetime.datetime.today())

    def available_to(self, user):
        # if no assigned users assume available to all
        if (not self.assigned_users.exists()):
            return True

        # if in assigned users it's available
        if (self.assigned_users.filter(id=user.id).exists()):
            return True

        return False

    def checkIfAvailable(self,datetime):

        if CheckIn.objects.filter(task=self):
            return False

        if self.date_available:
            if self.date_available_to:
                if self.date_available < datetime.date() <= self.date_available_to:
                    return True
                else:
                    return False
            elif self.date_available != datetime.date():
                return False
            ## check time
            return True

        # below happens if no date_available set
        day_of_week_of_date=datetime.weekday()
        
        days = {
            0: self.monday,
            1: self.tuesday,
            2: self.wednesday,
            3: self.thursday,
            4: self.friday,
            5: self.saturday,
            6: self.sunday,
        }

        if days[day_of_week_of_date] == True:
            return True

        return False

    @property
    def has_been_checked_in_on(self):

        if self.checkins.all():
            return True

        return False


class Approval(models.Model):
    approver = models.ForeignKey('tribe.TribeUser', related_name = "approvals")
    date_approved = models.DateField(auto_now=True)

def get_image_path(instance, filename):
    return os.path.join('static', 'photos', 'checkins', filename)

class CheckIn(models.Model):
    user = models.ForeignKey('tribe.TribeUser', related_name="checkins")
    task = models.ForeignKey(Task, related_name="checkins")
    date = models.DateTimeField()
    points_awarded = models.IntegerField()
    approval = models.OneToOneField(Approval, null=True)
    image = models.ImageField(upload_to="tribe/static/tribe/photos/checkins", blank=True, null=True)

    @property
    def has_been_approved(self):

        if self.approval:
            return True

        return False

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('checkin_detail', args=[str(self.id)])
        

class Reward(models.Model):
    
    tribe = models.ForeignKey('tribe.Tribe', related_name = "rewards")
    name = models.CharField(max_length = 20)
    description = models.CharField(max_length = 200)
    available_to = models.ManyToManyField(
                                        'tribe.TribeUser',
                                        related_name="available_rewards",
                                        )
    points_required = models.IntegerField()


class AchievedReward(models.Model):

    reward = models.ForeignKey('points.Reward', related_name = "wins")
    datetime=models.DateTimeField(auto_now=True)
    user = models.ForeignKey('tribe.TribeUser', related_name="achieved_rewards")

class RewardCashIn(models.Model):
    achievedReward = models.ForeignKey('points.AchievedReward', related_name='cashins')
    datetime=models.DateTimeField(auto_now=True)
