from rest_framework import serializers
from ads.models import Ad

class Serializer(serializers.ModelSerializer):
   class Meta:
       model = Ad
       exclude = ["id"]

       
