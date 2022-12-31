from django.db import models

class Categorie(models.Model):
    name = models.CharField(max_length=100, unique=True)


    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    def __str__(self):
        return self.name