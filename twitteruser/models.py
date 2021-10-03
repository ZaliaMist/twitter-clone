from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    following = models.ManyToManyField("self", symmetrical=False)
    display_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
