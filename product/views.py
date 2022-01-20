# from django.shortcuts import render
# from django.views.generic import ListView, DetailView
# from .models import Exportal_Product, Internal_Product
#
#
# # Create your views here.
# class Internal_Product_List(ListView):
#     queryset = Internal_Product.objects.filter(is_line=True)
#     template_name = "product/site/internal_list.html"
#     context_object_name = "Internal_Products"
#
#
# class Internal_Product_Detail(DetailView):
#     model = Internal_Product
#     template_name = "product/site/internal_detail.html"
#     slug_field = "id"
#     slug_url_kwarg = "id"
#     context_object_name = "Internal"
#
#
# class Exportal_Product_List(ListView):
#     model = Exportal_Product
#     template_name = "product/site/exportal_list.html"
#     context_object_name = "Exportal_Products"
#
#
# class Exportal_Product_Detail(DetailView):
#     model = Exportal_Product
#     template_name = "product/site/exportal_detail.html"
#     slug_field = "id"
#     slug_url_kwarg = "id"
#     context_object_name = "Exportal"
