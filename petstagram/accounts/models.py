from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, PermissionsMixin
from django.db import models

from cloudinary import models as cloudinary_models

from petstagram.accounts.managers import PetstagramUserManager


class PetstagramUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(auto_now_add=True, )

    USERNAME_FIELD = 'email'

    objects = PetstagramUserManager()


class Profile(models.Model):
    profile_image = cloudinary_models.CloudinaryField(
        resource_type='image',
        blank=True,
    )
    user = models.OneToOneField(
        PetstagramUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )


from .signals import *
