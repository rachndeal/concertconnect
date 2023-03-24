from django.contrib import admin

# Register your models here.
from concertconnect_app.models import Category, Page
from concertconnect_app.models import UserProfile

admin.site.register(UserProfile)



class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'url','description','views',)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    

admin.site.register(Page, PageAdmin) 
admin.site.register(Category, CategoryAdmin)