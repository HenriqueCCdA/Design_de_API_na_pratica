from django.urls import re_path

from coffeeApi.level2 import views


urlpatterns = [
    re_path(r'order(?:/(?P<id>\d+))?', views.dispatch),
]