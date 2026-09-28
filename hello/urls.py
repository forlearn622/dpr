from django.contrib import admin
from django.urls import path
from hello.views import show,login

urlpatterns = [
    # path('',sh),
    path('', show,name='home'),
    path('login/',login,name='login')

]