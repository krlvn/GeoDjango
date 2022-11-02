from django.urls import path
from django.views.generic import TemplateView

from .apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path('', TemplateView.as_view(template_name='mainapp/home.html'), name='home'),
]
