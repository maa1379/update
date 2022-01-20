from django.urls import path

from .views import MineListView, MineDetailView, MineCreateView

app_name = "mine"
urlpatterns = [
    path("mine_list/", MineListView.as_view(), name="mine_list"),
    path("mine_detail/<int:id>/", MineDetailView.as_view(), name="mine_detail"),
    path("mine_create/", MineCreateView.as_view(), name="mine_create"),
]
