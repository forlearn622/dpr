from django.contrib import admin
from bollywood.models import movies

# Register your models here.
@admin.register(movies)
class moviesAdmin(admin.ModelAdmin):
    list_display = ('id','name','release_date','box_office')

# admin.site.register(movies, moviesAdmin)    
