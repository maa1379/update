from django.shortcuts import render
from product.models import Exportal_Product
from django.views.generic import View


# Create your views here.


class SiteMain(View):
    def get(self, request):
        pass


def Home(request):
    return render(request, "site/Home.html")
