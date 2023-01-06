from django.db import models

from categories.models import Categorie
from user.models import User




class Ad(models.Model):
    name= models.CharField(max_length=100, verbose_name="Название")
    author= models.ForeignKey(User, related_name='ads',on_delete=models.CASCADE)
    price= models.IntegerField()
    description= models.CharField(max_length=1000)
    is_published= models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Categorie,related_name = 'category' ,on_delete=models.NOT_PROVIDED,null=True)


    class Meta:
        verbose_name = "Обьявление"
        verbose_name_plural = "Обьявлении"
    def __str__(self):
        return self.name
    @property
    def first_name(self):
        return self.author.first_name if self.author else None



class Compilation(models.Model):

    author = models.ForeignKey(User,on_delete=models.CASCADE )
    name = models.CharField(max_length=200)
    ads = models.ManyToManyField(Ad,null=True)

    class Meta:
        verbose_name = "Подборка"
        verbose_name_plural = "Подборки"

    def __str__(self):
        return self.author.username