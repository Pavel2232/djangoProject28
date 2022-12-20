import json

from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

import ads
from djangoProject272 import settings
from location.models import Location
from user.models import User



@method_decorator(csrf_exempt, name='dispatch')
class UserView(ListView):
    model = User

    def get(self,request,*args,**kwargs):
        super().get(request,*args,**kwargs)

        self.object_list = self.object_list.order_by("username")

        response = []
        for user in self.object_list:
            response.append({
            "first_name" : user.first_name,
            "last_name" : user.last_name,
            "username" : user.username,
            "role" : user.role,
            "total_ads" : user.ads.filter(is_published= True).count()})

        return JsonResponse(response,safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(CreateView):
    model = User
    fields = '__all__'
    success_url = '/'





@method_decorator(csrf_exempt, name='dispatch')
class UserDetailView(DetailView):
    model = User

    def get(self,request,*args,**kwargs):

        users = self.get_object()

        return JsonResponse({
            "first_name" : users.first_name,
            "last_name" : users.last_name,
            "username" : users.username,
            "role" : users.role,
            "location" : list(map(str,users.location.all()))})

@method_decorator(csrf_exempt, name='dispatch')
class UserPatchView(UpdateView):
    model = User
    fields = [ "first_name", "last_name", "username","password" , "role","age" ,"location"]

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)


        user_data = json.loads(request.body)

        if "first_name" in user_data.keys():
            self.object.first_name = user_data["first_name"]

        if "last_name" in user_data.keys():
            self.object.last_name = user_data["last_name"]

        if "username" in user_data.keys():
            self.object.username = user_data["username"]

        if "password" in user_data.keys():
            self.object.password = user_data["password"]

        if "role" in user_data.keys():
            self.object.role = user_data["role"]

        if "age" in user_data.keys():
            self.object.age = user_data["age"]

        if "location" in user_data.keys():
            for loc_name in user_data['location']:
                loc, _ = Location.objects.get_or_create(name= loc_name)
                self.object.location.add(loc)


        self.object.save()

        return JsonResponse({
            "first_name" : self.object.first_name,
            "last_name" : self.object.last_name,
            "username" : self.object.username,
            "password" : self.object.password,
            "role" : self.object.role,
            "age" : self.object.age,
            "location" : list(self.object.selected_related('user').prefetch_related('location')),
            "total_ads" : self.object.ads.filter(is_published= True).count()},
        safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class UserDeleteView(DeleteView):
    model = User
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)



