
from django.db.models import Q
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from ads.models import Ad, Compilation
from ads.permissions import  UserPermission, UserPathchrmission
from ads.serializer import AdListSerializer, AdRetrieveSerializer, AdCreateSerializer, AdUpdateSerializer, \
    AdDestroyserializer, CompilationSerializer, CompilationRetrieveSerializer, CompilationCreateSerializer, \
    CompilationUpdateSerializer, CompilationDestroySerializer


class IndexView(ListAPIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse({"status": "200"}, safe=False)


class AdCreateView(CreateAPIView):
    queryset = Ad
    serializer_class = AdCreateSerializer
    permission_classes = [IsAuthenticated]



class AdView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializer


    def get(self, request, *args, **kwargs):
        ads_id = request.GET.getlist("category")
        ads_name = request.GET.get("name")
        ads_location = request.GET.get("location")
        ads_price = request.GET.getlist("price")
        if ads_id:
            self.queryset = self.queryset.filter(category__id__in = ads_id)


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
    permission_classes = [IsAuthenticated]



class AdUpdateView(UpdateAPIView):
   queryset = Ad
   serializer_class = AdUpdateSerializer


class AdDestroyView(DestroyAPIView):
    queryset = Ad
    serializer_class = AdDestroyserializer
    permission_classes = (UserPermission,)
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



class CompilationListView(ListAPIView):
    queryset = Compilation.objects.all()
    serializer_class = CompilationSerializer


class CompilationRetrieveView(RetrieveAPIView):
    queryset = Compilation
    serializer_class = CompilationRetrieveSerializer


class CompilationCreateView(CreateAPIView):
    queryset = Compilation
    serializer_class = CompilationCreateSerializer
    permission_classes = [IsAuthenticated]

class CompilationUpdateView(UpdateAPIView):
    queryset = Compilation
    serializer_class = CompilationUpdateSerializer
    permission_classes = (UserPathchrmission,)
class CompilationDestroyView(DestroyAPIView):
    queryset = Compilation
    serializer_class = CompilationDestroySerializer
    permission_classes = (UserPermission,)
