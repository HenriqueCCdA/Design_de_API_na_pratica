from django.urls import path

from coffeeApi.level0.views import barista


urlpatterns = [
    path('PlaceOrder', barista)
]