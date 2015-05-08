from django.contrib.auth.models import BaseUserManager

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
