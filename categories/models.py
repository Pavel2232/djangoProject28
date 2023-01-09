from django.core.exceptions import ValidationError
from django.db import models


def chek_len_slug(value: str):
    if len(value) <= 5:
        raise ValidationError(
            f"{value} или слишком короткое название",
            params = {'value': value} ,
        )
    elif len(value) > 10 :
        raise ValidationError(
            f"{value} слишком длинное название",
            params={'value': value},
        )

class Categorie(models.Model):
    slug = models.CharField(max_length=100, unique=True,validators=[chek_len_slug])


    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    def __str__(self):
        return self.slug