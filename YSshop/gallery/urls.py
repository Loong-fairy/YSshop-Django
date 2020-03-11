from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('add/', add, name='add'),
    path('detail/', detail, name='detail'),
    path('error/', error, name='error'),
    path('login/', login, name='login'),
    path('register/', register, name='register')
]
