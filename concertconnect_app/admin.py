from django.contrib import admin
from rango.models import UserProfile, Concert, Review

# Register your models here.
from concertconnect_app.models import Category, Page
from concertconnect_app.models import UserProfile

admin.site.register(UserProfile)



class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'url')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    

admin.site.register(Page, PageAdmin) 
admin.site.register(Category, CategoryAdmin)