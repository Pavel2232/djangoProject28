from django.urls import path


from ads import views

urlpatterns = [
    path('', views.AdView.as_view(), name="ad"),
    path('<int:pk>/',views.AdDetailView.as_view(), name="ad-pk"),
    path('<int:pk>/patch/',views.AdPatchView.as_view(), name="update_data"),
    path('create/',views.AdCreateView.as_view(), name="update_data"),
    path('<int:pk>/delete/',views.AdDeleteView.as_view(), name="delete"),
    path('<int:pk>/upload_image/',views.Image.as_view(), name="ImageUp"),
]