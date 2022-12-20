import json

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView

from categories.models import Categorie


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class CatView(ListView):
    model = Categorie
    def get(self,request,*args,**kwargs):
        super().get(request,*args,**kwargs)

        self.object_list = self.object_list.order_by("name")

        response = []
        for ad in self.object_list:
            response.append({
            "id" : ad.id,
            "name" : ad.name,
            })
        return JsonResponse(response,safe=False)

    def post(self,request):
        cat_data = json.loads(request.body)

        ad = Categorie.objects.create(
            name=cat_data["name"],
            )


        return JsonResponse({
            "id" : ad.id,
            "name" : ad.name,},safe=False)


class CatDetailView(DetailView):
    model = Categorie

    def get(self,request,*args,**kwargs):

        categories = self.get_object()

        return JsonResponse({
            "id" : categories.id,
            "name" : categories.name,
             })