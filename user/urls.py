from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from user import views

urlpatterns = [
    path('create', views.UserCreateView.as_view(), name="create-user"),
    path('token/', TokenObtainPairView.as_view(), name = "Token"),
    path('token/refresh/', TokenRefreshView.as_view(), name = "RefreshToken"),

]