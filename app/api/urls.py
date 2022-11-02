from django.urls import path

from .apps import ApiConfig
from . import views

app_name = ApiConfig.name

urlpatterns = [
    path('', views.GetNeighboursView.as_view()),
]
