from rest_framework import serializers

class Serializer(serializers.ModelSerializer):
   class Meta:
       model = Ad
       exclude = ["id"]

       
