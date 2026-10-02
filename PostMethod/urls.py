from django.urls import path
from PostMethod.views import stu_reg,reg_suc

urlpatterns = [
    path('regi/',stu_reg,name = 'stu_reg'),    
    path('suc/',reg_suc,name = 'success')

]
