from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('', views.nav),
    path('home/', views.home),
    path('product/<int:id>', views.findProduct),
    path('category/<int:id>', views.filterCategory)
]