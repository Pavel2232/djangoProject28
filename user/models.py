from django.contrib.auth.models import AbstractUser
from django.db import models

from location.models import Location


class User(AbstractUser):
    MEMBER = "member"
    ADMIN = "admin"
    MODERATOR = "moderator"


    ROLE = [
        (MEMBER,"member"),
        (ADMIN,"admin"),
        (MODERATOR,"moderator")
    ]
    SEX = [("Men", "Мужской"),
           ("Women","Женский"),
           ]

    role = models.CharField(max_length=100,choices= ROLE, default="member")
    sex = models.CharField(max_length=8, choices= SEX, default="Man")
    location = models.ManyToManyField(Location,null=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.username}"