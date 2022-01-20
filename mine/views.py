from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Mine
from django.urls import reverse_lazy
from .forms import MineForm


# Create your views here.
class MineListView(ListView):
    model = Mine
    template_name = "mine/site/mine_list.html"


class MineDetailView(DetailView):
    model = Mine
    slug_field = "id"
    slug_url_kwarg = "id"
    template_name = "mine/site/mine_detail.html"
    context_object_name = "Mine"


class MineCreateView(CreateView):
    model = Mine
    form_class = MineForm
    success_url = reverse_lazy()
    template_name = "mine/panel/mine_create.html"
