from django.urls import path

from . import views
from django.conf import settings


urlpatterns = [
    path('', views.blog, name='blog'),
    path('categoria/<int:categoria_id>/', views.categoria, name='categoria'),
]

