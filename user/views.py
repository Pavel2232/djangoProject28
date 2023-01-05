from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet, ViewSet

from user.models import User
from user.serializer import UserCreateSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


