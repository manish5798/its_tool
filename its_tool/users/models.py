from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.db.models import CharField
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """Creates and saves a new superuser"""
        user = self.create_user(email, password)
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    """Default user for ssss"""

    email = CharField(_("Email of User"), blank=False, unique=True, max_length=255)
    mobile = CharField(_("Mobile of User"), blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


@receiver(pre_save, sender=User)
def update_username_from_email(sender, instance, **kwargs):
    instance.username = instance.email


def profile_picture_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return "user/profile/{}.{}".format(filename, "jpg")


class Address(models.Model):
    address_1 = models.CharField(max_length=255, blank=True, null=True)
    address_2 = models.CharField(max_length=255, blank=True, null=True)
    locality_area = models.CharField(max_length=255, blank=True, null=True)
    landmark = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=False)
    state = models.CharField(max_length=255, blank=False)
    country = models.CharField(max_length=255, blank=True)
    zip_code = models.CharField(max_length=255, blank=True, null=True)
    address_type = models.CharField(max_length=255, null=True, blank=True)


class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), related_name="user_profile", primary_key=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    gender = models.CharField(max_length=255, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(null=True)
    is_verified = models.BooleanField(null=True)
    profile_picture = models.FileField(upload_to=profile_picture_directory_path, max_length=254, blank=True, null=True)
    timezone = models.CharField(max_length=255, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    mobile = models.CharField(max_length=255, null=True)
