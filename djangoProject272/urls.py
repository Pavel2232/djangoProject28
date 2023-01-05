"""djangoProject272 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from ads.views import IndexView, CompilationListView
from categories.views import CategoryViewSet
from djangoProject272 import settings
from location.views import LocationViewSet

router= routers.SimpleRouter()
router.register(r'location', LocationViewSet)
router.register(r'category',CategoryViewSet)

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('admin/', admin.site.urls),
    path('ad/', include('ads.urls'), name = "ad"),
    path('user/', include('user.urls'), name = "user"),
    path('selection/', CompilationListView.as_view(), name = "Compilation"),
   ]

urlpatterns += router.urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
