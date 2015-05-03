from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.core.urlresolvers import reverse
from points.models import Approval
from points.models import Category
import datetime

class TribeUserManager(BaseUserManager):

    def create(self, email, password=None, name="User"):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name
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
            name = "Superuser"
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class TribeManager(BaseUserManager):

    def create(self, name="My Tribe"):

        tribe = self.model(
            name=name,
        )

        tribe.save()

        # create some default categories
        tribe.categories.create(tribe=tribe,
                                name="Household",
                                description="Jobs around the house.")
        tribe.categories.create(tribe=tribe,
                                name="Pets",
                                description="The animals of the house.")
        tribe.categories.create(tribe=tribe,
                                name="School",
                                description="School and homework.")
        tribe.categories.create(tribe=tribe,
                                name="Sports and fitness",
                                description="All sports",)

        # create some default tasks
        tribe.tasks.create(
            tribe = tribe,
            name = "Take out the bins",
            description = "Put the green and black bins out on the road.", 
            category = Category.objects.get(tribe=tribe, name="Household"),
            points_reward = 20, 
            monday = True, 
            tuesday = False,
            wednesday = False,
            thursday = False,
            friday = False,
            saturday = False,
            sunday = True,
        )

        tribe.tasks.create(
            tribe = tribe,
            name = "Take the dogs for a walk.",
            description = "At least 15 mins.", 
            category = Category.objects.get(tribe=tribe, name="Pets"),
            points_reward = 40, 
            monday = True, 
            tuesday = True,
            wednesday = True,
            thursday = True,
            friday = True,
            saturday = True,
            sunday = True,
        )

        tribe.tasks.create(
            tribe = tribe,
            name = "Put on a laundry wash.",
            description = "Empty the linen baskets from all bedrooms.", 
            category = Category.objects.get(tribe=tribe, name="Household"),
            points_reward = 15, 
            monday = True, 
            tuesday = True,
            wednesday = True,
            thursday = True,
            friday = True,
            saturday = True,
            sunday = True,
        )

        tribe.tasks.create(
            tribe = tribe,
            name = "Feed the dogs.",
            description = "One can of pedigree chum each.", 
            category = Category.objects.get(tribe=tribe, name="Pets"),
            points_reward = 15, 
            monday = True, 
            tuesday = True,
            wednesday = True,
            thursday = True,
            friday = True,
            saturday = True,
            sunday = True,
        )

        tribe.tasks.create(
            tribe = tribe,
            name = "Make bed.",
            description = "Make own bed.", 
            category = Category.objects.get(tribe=tribe, name="Household"),
            points_reward = 5, 
            monday = True, 
            tuesday = True,
            wednesday = True,
            thursday = True,
            friday = True,
            saturday = True,
            sunday = True,
        )

        tribe.tasks.create(
            tribe = tribe,
            name = "Tidy bedroom.",
            description = "Take everything off floor, dirty clothes in laundry basket.", 
            category = Category.objects.get(tribe=tribe, name="Household"),
            points_reward = 10, 
            monday = True, 
            tuesday = True,
            wednesday = True,
            thursday = True,
            friday = True,
            saturday = True,
            sunday = True,
        )

        tribe.tasks.create(
            tribe = tribe,
            name = "Brush teeth",
            description = "Brush teeth with toothpaste in bathroom.",
            category = Category.objects.get(tribe=tribe, name="Household"),
            points_reward = 5, 
            monday = True, 
            tuesday = True,
            wednesday = True,
            thursday = True,
            friday = True,
            saturday = True,
            sunday = True,
        )

        tribe.tasks.create(
            tribe = tribe,
            name = "Do homework",
            description = "Every subject. Check homework journal.",
            category = Category.objects.get(tribe=tribe, name="School"),
            points_reward = 30, 
            monday = True, 
            tuesday = True,
            wednesday = True,
            thursday = True,
            friday = True,
            saturday = True,
            sunday = True,
        )

        return tribe

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


class InvitedUser(models.Model):

    def __str(self):
        return email

    email = models.EmailField(unique=True)
    tribe = models.ForeignKey(Tribe, related_name='invited_users')

    def save(self, *args, **kwargs):
        super(InvitedUser, self).save(*args, **kwargs)
        # now email the new user

def get_image_path(instance, filename):
    return os.path.join('static', 'photos', 'users', filename)

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
