from django.urls import path

from categories import views

urlpatterns = [
    path('', views.CatView.as_view(), name="ad"),
    path('<int:pk>/',views.CatDetailView.as_view(), name="ad-pk"),
]