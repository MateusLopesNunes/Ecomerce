from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home/', views.home),
    path('product/<int:id>', views.findProduct),
]