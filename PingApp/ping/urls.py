from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('all', views.all),
    path('online', views.online),
    path('offline', views.offline),
    path('uefi', views.uefi),
    path('create', views.create)
]