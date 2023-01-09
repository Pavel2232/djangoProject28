import datetime

from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from user.models import User


def chek_email(email):
    response =email.rsplit("@", 1)
    need_email = response[-1]

    if need_email == 'rambler.ru':
        raise serializers.ValidationError(f'{email} нельзя зарегистрироваться с почтой rambler')


class NotDataValid:
    def __init__(self,data):
        self.year = data.year
    def __call__(self,value):

        if self.year < value.year:
            raise serializers.ValidationError(f'нельзя зарегистрироваться младше 9 лет')



class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[chek_email])
    birth_date = serializers.DateField(validators=[NotDataValid(datetime.date(2014,1,1))])
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user= User(**validated_data)

        user.password = make_password(validated_data["password"])

        user.save()

        return user