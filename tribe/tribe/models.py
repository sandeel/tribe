from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.core.urlresolvers import reverse

class TribeUserManager(BaseUserManager):

    def create(self, email, password=None):

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
        user = self.create(email,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Tribe(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class InvitedUser(models.Model):

    def __str(self):
        return email

    email = models.EmailField(unique=True)
    tribe = models.ForeignKey(Tribe, related_name='invited_users')

    def save(self, *args, **kwargs):
        super(InvitedUser, self).save(*args, **kwargs)
        # now email the new user

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

    tribe = models.ForeignKey(Tribe, null=True, related_name ='members', on_delete=models.SET_NULL)
    leader_of = models.ForeignKey(Tribe, null=True, related_name='leaders')

    USERNAME_FIELD = 'email'

    def save(self, *args, **kwargs):
        if not self.pk:
            #This code only happens if the objects is
            #not in the database yet. Otherwise it would
            #have pk

            # handle adding to a tribe
            invited_emails = InvitedUser.objects.values_list('email', flat=True)
            if (self.email in invited_emails):
                invitedUser = InvitedUser.objects.get(email=self.email)
                self.tribe = invitedUser.tribe
                invitedUser.delete()
            
            super(TribeUser, self).save(*args, **kwargs)


    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
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
        new_tribe.members.add(self)

    def promote_to_leader(self):
        if self.tribe == None:
            return False

        self.tribe.leaders.add(self)

    def demote_from_leader(self):
        if self.tribe == None:
            return False

        self.tribe.leaders.remove(self)
