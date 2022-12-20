from django.db import models

# Create your models here.
class Categorie(models.Model):
    name = models.CharField(max_length=100)


    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    def __str__(self):
        return self.name