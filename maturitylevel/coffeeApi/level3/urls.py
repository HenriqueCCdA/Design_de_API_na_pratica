from django.urls import re_path, path

from coffeeApi.level3 import views


urlpatterns = [
    re_path(r'order(?:/(?P<id>\d+))?', views.dispatch, name='order'),
    path('payment/<int:id>', views.payment, name='payment'),
    path('receipt/<int:id>', views.receipt, name='receipt')
]