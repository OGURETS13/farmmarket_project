from django.urls import path, include

from . import views


app_name = 'mail'

urlpatterns = [
    path('', views.index, name='index'),
    path('function1/', views.function1, name='function1')
]
