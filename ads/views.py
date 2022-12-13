import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView

from ads.models import Ad


# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class IndexView(view):
    def get(self, request,*args,**kwargs):
        return JsonResponse({"status": "200"}, safe= False)


class AdView(ListView):
    def get(self,request,*args,**kwargs):
        ads_query = Ad.objects.all()

        response = [{"Response" : "200"}]
        for ad in ads_query:
            response.append({
            "name" : ad.name,
            "author" : ad.author,
            "price" : ad.price,
            })
        return JsonResponse(response,safe=False)

    def post(self,request):
        ad_data = json.loads(request.body)

        ad = Ad.objects.create(
            name=ad_data["name"],
            author = ad_data["author"],
            price= ad_data["price"],
            description = ad_data["description"],
            address= ad_data["address"],
            is_published= ad_data["is_published"],
            )


        return JsonResponse({
            "name" : ad.name,
            "author" : ad.author,
            "price" : ad.price},safe=False)


class AdDetailView(DetailView):
    model = Ad

    def get(self,request,*args,**kwargs):

        ads = self.get_object()

        return JsonResponse({
            "name" : ads.name,
            "author" : ads.author,
            "price" : ads.price,
            "description" : ads.description,
            "address" : ads.address,
            "is_published" : ads.is_published})
