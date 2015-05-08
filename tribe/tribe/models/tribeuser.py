from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from tribe.models.tribeusermanager import TribeUserManager
from tribe.models.tribe import Tribe
from tribe.models.inviteduser import InvitedUser

class TribeUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=40,null=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = TribeUserManager()

    tribe = models.ForeignKey(Tribe, null=False, related_name ='members')
    leader_of = models.ForeignKey(Tribe, null=True, related_name='leaders')

    USERNAME_FIELD = 'email'

    image = models.ImageField(upload_to="tribe/static/tribe/photos/user_profiles", blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            #This code only happens if the objects is
            #not in the database yet. Otherwise it would
            #have pk

            # handle adding to a tribe if invited
            invited_emails = InvitedUser.objects.values_list('email', flat=True)
            if (self.email in invited_emails):
                invitedUser = InvitedUser.objects.get(email=self.email)
                self.tribe = invitedUser.tribe
                invitedUser.delete()
            else:
                tribe_name = (self.name + "'s tribe")
                self.tribe = Tribe.objects.create(name=tribe_name)
                self.leader_of = self.tribe
            
        super(TribeUser, self).save(*args, **kwargs)


    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    @property
    def url(self):
        return reverse("tribemembers", args=[self.id])

    @property
    def is_leader(self):
        if self.tribe == None:
            return False

        return self.id in self.tribe.leaders.all().values_list('id',flat=True)

    def add_to_tribe(self, new_tribe):
        old_tribe = self.tribe
        new_tribe.members.add(self)
        if old_tribe.members.count() == 0:
            old_tribe.delete()

    def promote_to_leader(self):
        if self.tribe == None:
            return False

        self.tribe.leaders.add(self)

    def demote_from_leader(self):
        if self.tribe == None:
            return False

        self.tribe.leaders.remove(self)

    @property
    def points(self):
        approvals = Approval.objects.filter(checkin__user=self)

        points = 0

        for approval in approvals:
            points += approval.checkin.points_awarded

        return points

    def get_absolute_url(self):
        return reverse('tribemembers', args=[str(self.id)])

        class Meta:
            db_table = 'tribeuser'
            app_label = 'tribe'
