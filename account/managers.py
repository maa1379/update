from django.contrib.auth.models import BaseUserManager
from .models import User


class MyUserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError('users must have Email')

        user = self.create_user(email=self.normalize_email(email), password=password)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user
