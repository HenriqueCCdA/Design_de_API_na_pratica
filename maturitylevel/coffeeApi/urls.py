from django.urls import path, include

urlpatterns = [
    path('', include('coffeeApi.level0.urls')),
    path('', include('coffeeApi.level1.urls')),
]