from django.db import models
from product.models import Exportal_Product, Internal_Product
from django.contrib.auth.models import AbstractBaseUser
from django.db.models.signals import post_save
from .managers import MyUserManager


# Create your models here.
class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = [""]
    USERNAME_FIELDS = "email"
    objects = MyUserManager()
    is_special_user = models.BooleanField(default=False)
    is_patient_user = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_panel_admin=models.BooleanField(default=False)

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="profile")
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    company_name = models.CharField(max_length=500, null=True, blank=True)
    activity_field = models.CharField(max_length=255, null=True, blank=True)
    position = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    create=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class FavoriteBaseMode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateField()

    class Meta:
        abstract = True


class UserFavoriteInternal(FavoriteBaseMode):
    product = models.ForeignKey(Internal_Product, on_delete=models.CASCADE)


class UserFavoriteExportal(FavoriteBaseMode):
    product = models.ForeignKey(Exportal_Product, on_delete=models.CASCADE)


def save_profile(sender, **kwargs):
    if kwargs['created']:
        p1 = Profile(user=kwargs['instance'])
        p1.save()


post_save.connect(save_profile, sender=User)
