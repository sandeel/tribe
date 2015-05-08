from django.db import models
from tribe.models.tribemanager import TribeManager

class Tribe(models.Model):
    objects = TribeManager()
    name = models.CharField(max_length=255, unique=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Tribe, self).save(*args, **kwargs)

    @property
    def total_points(self):
        approvals = Approval.objects.filter(checkin__user__tribe=self)

        points = 0

        for approval in approvals:
            points += approval.checkin.points_awarded

        return points

    def points_on_date(self, date):
        approvals = Approval.objects.filter(checkin__user__tribe=self, date_approved=date)

        points = 0

        for approval in approvals:
            points += approval.checkin.points_awarded

        return points

    @property
    def points_for_week_so_far(self):
        today = datetime.date.today()

        the_last_monday = today - datetime.timedelta(days=today.weekday())

        points = []

        for x in range(0,7):
            date = the_last_monday + datetime.timedelta(days=x)
            points_on_date = self.points_on_date(date)
            points.append(points_on_date)

        return points

    @property
    def points_this_week(self):
        return sum(self.points_for_week_so_far)

    @property
    def points_today(self):
        today = datetime.date.today()

        points = self.points_on_date(today)

        return points

