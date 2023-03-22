from django.urls import path
from concertconnect_app import views
from . import views
from django.urls import include, path
from django.conf.urls import url

app_name = 'concertconnect_app'

urlpatterns = [
	path('', views.index, name='index'),
    
	path('concerts/', views.concerts, name='concerts'),
    
    
    path('about/', views.about, name='about'),
    
    path('category/<slug:category_name_slug>/',views.show_category, name='show_category'),
    
    path('add_category/', views.add_category, name='add_category'),

    path('category/<slug:category_name_slug>/add_page/',views.add_page, name='add_page'),
    path('restricted/', views.restricted, name='restricted'),
    path('search/', views.search_bar, name='search'),
    path('goto/', views.goto_url, name='goto'),
    path('register_profile/', views.register_profile, name='register_profile'),
]