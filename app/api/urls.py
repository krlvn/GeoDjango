from django.urls import path
from . import views

urlpatterns = [
    path('', views.GetNeighbours.as_view()),
]
