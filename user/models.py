from django.db import models

from location.models import Location


class User(models.Model):
    ROLE = [
        ("member","пользователь"),
        ("admin","администратор"),
        ("moderator","модератор")
    ]

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=300)
    username = models.CharField(max_length=300)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=100,choices= ROLE, default="member")
    age = models.IntegerField()
    location = models.ManyToManyField(Location)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.username}  {self.last_name}"