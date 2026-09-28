from django.contrib import admin
from hello.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','age')

admin.site.register(Student,StudentAdmin)