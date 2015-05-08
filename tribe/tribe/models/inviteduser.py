from django.db import models
from tribe.models.tribe import Tribe

class InvitedUser(models.Model):

    def __str(self):
        return self.email

    email = models.EmailField(unique=True)
    tribe = models.ForeignKey(Tribe, related_name='invited_users')

    def save(self, *args, **kwargs):
        super(InvitedUser, self).save(*args, **kwargs)
        # now email the new user

