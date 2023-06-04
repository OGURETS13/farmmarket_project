from django.urls import path, include

from . import views


app_name = 'mail'

urlpatterns = [
    path('', views.index, name='index'),
    path('order_paid/', views.order_paid, name='order_paid'),
    path(
        'registration_email/',
        views.registration_email,
        name='registration_email'
    )
]
