from django.urls import path
from bollywood.views import bolly,register

urlpatterns = [
    # path('',sh),
    path('bolly/', bolly,name='bolly_mov'),
    path('register/',register,name='register')

]