from django.urls import path
from entertainment.views import type_ent,ent_suc

urlpatterns = [
    path('ent/',type_ent,name='entainment'),
    path('ent_suc/',ent_suc,name = 'ent_suc')

]