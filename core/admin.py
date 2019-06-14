from django.contrib import admin
from .models import MainPage

class MainPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
    search_fields = ['title', 'sub_title', 'body']
    prepopulated_fields = {"slug": ("title",)}

# Register your models here.
admin.site.register(MainPage, MainPageAdmin)
