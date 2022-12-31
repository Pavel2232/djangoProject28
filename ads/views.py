import json

from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from ads.models import Ad
from ads.serializer import AdListSerializer, AdRetrieveSerializer, AdCreateSerializer, AdUpdateSerializer, \
    AdDestroyserializer
from djangoProject272 import settings


class IndexView(ListAPIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse({"status": "200"}, safe=False)


class AdCreateView(CreateAPIView):
    queryset = Ad
    serializer_class = AdCreateSerializer



class AdView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializer


    def get(self, request, *args, **kwargs):
        ads_id = request.GET.getlist("category",None)
        ads_name = request.GET.get("name",None)
        ads_location = request.GET.get("location",None)
        ads_price = request.GET.getlist("price",None)
        ads_q_id = None
        for ad in ads_id:
            if ads_q_id is None:
                ads_q_id = Q(category__id__contains= ad)
            else:
                ads_q_id |= Q(category__id__contains= ad)
        if ads_q_id:
            self.queryset = self.queryset.filter(ads_q_id)


        if ads_name:
            self.queryset = self.queryset.filter(name__icontains=ads_name)

        if ads_location:
            self.queryset = self.queryset.filter(author__location__name__icontains=ads_location)

        ads_q_price = None
        for ad in ads_price:
            if ads_q_price is None:
                ads_q_price = Q(price__gte= ad)
            else:
                ads_q_price |= Q(price__lte= ad)
        if ads_q_price:
            self.queryset = self.queryset.filter(ads_q_price)

        return super().get(request, *args, **kwargs)




class AdDetailView(RetrieveAPIView):
    queryset = Ad
    serializer_class = AdRetrieveSerializer



class AdUpdateView(UpdateAPIView):
   queryset = Ad
   serializer_class = AdUpdateSerializer


class AdDestroyView(DestroyAPIView):
    queryset = Ad
    serializer_class = AdDestroyserializer


@method_decorator(csrf_exempt, name='dispatch')
class Image(UpdateView):
    model = Ad

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.image = request.FILES['image']
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "image": self.object.image.url if self.object.image else None,

        })
