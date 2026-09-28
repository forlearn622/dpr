from django.urls import path
from welcome.views import eng_greet,usa_greet,series


urlpatterns = [
    path('e/', eng_greet,name='movies'),
    path('u/',usa_greet,name='anime'),
    path('s/',series,name='series'),

]