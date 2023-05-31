from django.urls import path, include

from . import views


app_name = 'mail'

urlpatterns = [
    path('', views.index, name='index'),
    path('order_paid/', views.function1, name='order_paid')
]
