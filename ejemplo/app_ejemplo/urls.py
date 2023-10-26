from django.urls import path
from app_ejemplo import views

urlpatterns = [
    path('inicio', views.index)
]
