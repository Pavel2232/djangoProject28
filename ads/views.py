import json

from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from ads.models import Ad
from djangoProject272 import settings


@method_decorator(csrf_exempt, name='dispatch')
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({"status": "200"}, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateView):
    model = Ad
    fields = '__all__'
    success_url = '/'


@method_decorator(csrf_exempt, name='dispatch')
class AdView(ListView):
    model = Ad

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        self.object_list = self.object_list.order_by("-price")

        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page = request.GET.get("page")
        page_obj = paginator.get_page(page)

        result = []
        for ad in page_obj:
            result.append({
                "name": ad.name,
                "author": ad.author.first_name,
                "price": ad.price,
            })

        response = {
            "items": result,
            "total": paginator.count,
            "num_page": paginator.num_pages,
        }

        return JsonResponse(response, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        ads = self.get_object()

        return JsonResponse({
            "name": ads.name,
            "author": ads.author.first_name,
            "price": ads.price,
            "description": ads.description,
            "is_published": ads.is_published})


@method_decorator(csrf_exempt, name='dispatch')
class AdPatchView(UpdateView):
    model = Ad
    fields = ["name", "author", "price", "description", "is_published", "image", "category"]

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        ads_data = json.loads(request.body)

        if "name" in ads_data.keys():
            self.object.name = ads_data["name"]

        if "author" in ads_data.keys():
            self.object.author = ads_data["author"]

        if "price" in ads_data.keys():
            self.object.price = ads_data["price"]

        if "description" in ads_data.keys():
            self.object.description = ads_data["description"]

        if "is_published" in ads_data.keys():
            self.object.is_published = ads_data["is_published"]

        if "image" in ads_data.keys():
            self.object.image = ads_data["image"]

        if "category" in ads_data.keys():
            self.object.category = ads_data["category"]

        try:
            self.object.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)

        self.object.save()

        return JsonResponse({
            "name": self.object.name,
            "author": self.object.author.first_name,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "image": self.object.image.url if self.object.image else None,
            "category": self.object.category.name, })


@method_decorator(csrf_exempt, name='dispatch')
class AdDeleteView(DeleteView):
    model = Ad
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)


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
