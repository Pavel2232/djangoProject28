from django.urls import path


from user import views

urlpatterns = [
    path('', views.UserView.as_view(), name="ad"),
    path('<int:pk>/',views.UserDetailView.as_view(), name="ad-pk"),
    path('<int:pk>/patch/',views.UserPatchView.as_view(), name="update_data"),
    path('create/',views.UserCreateView.as_view(), name="update_data"),
    path('<int:pk>/delete/',views.UserDeleteView.as_view(), name="delete"),
]