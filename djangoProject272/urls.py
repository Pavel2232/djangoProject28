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

from ads.views import IndexView
from categories.views import CatView, CatDetailView
from djangoProject272 import settings

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('admin/', admin.site.urls),
    path('ad/', include('ads.urls'), name = "ad"),
    path('cat/', include('categories.urls'), name="categorie"),
    path('user/', include('user.urls'), name="user"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
