from django.urls import path

from level0.core.views import barista


urlpatterns = [
    path('PlaceOrder', barista),
]
