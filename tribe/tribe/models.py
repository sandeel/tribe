from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.core.urlresolvers import reverse

class TribeUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Tribe(models.Model):
    name = models.CharField(max_length=30)

class InvitedEmail(models.Model):

    def __unicode__(self):
        return email

    email = models.EmailField()
    tribe = models.ForeignKey(Tribe, related_name='invited_emails')

class TribeUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=40)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = TribeUserManager()

    tribe = models.ForeignKey(Tribe, null=True, related_name ='members')
    leader_of = models.ForeignKey(Tribe, null=True, related_name='leaders')

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

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
        new_tribe.members.add(self)

    def promote_to_leader(self):
        if self.tribe == None:
            return False

        self.tribe.leaders.add(self)

    def demote_from_leader(self):
        if self.tribe == None:
            return False

        self.tribe.leaders.remove(self)
