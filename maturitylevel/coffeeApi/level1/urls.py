from django.urls import path

from coffeeApi.level1 import views


urlpatterns = [
    path('order/create', views.create),
    path('order/delete', views.delete),
    path('order/update', views.update),
    path('order', views.read),
]