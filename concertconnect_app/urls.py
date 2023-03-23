from django.urls import path
from concertconnect_app import views
from . import views
from django.urls import include, path
from django.conf.urls import url

app_name = 'concertconnect_app'

urlpatterns = [
	
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('concerts/', views.ConcertsView.as_view(), name='concerts'),
    path('category/<slug:category_name_slug>/', views.ShowCategoryView.as_view(), name='show_category'),
    path('add_category/', views.AddCategoryView.as_view(), name='add_category'),
    path('category/<slug:category_name_slug>/add_page/', views.AddPageView.as_view(), name='add_page'),
    path('restricted/', views.RestrictedView.as_view(), name='restricted'),
    path('goto/', views.GotoView.as_view(), name='goto'),
    path('register_profile/', views.RegisterProfileView.as_view(), name='register_profile'),
    path('profile/<username>/', views.ProfileView.as_view(), name='profile'),
    path('profiles/', views.ListProfilesView.as_view(), name='list_profiles'),
    path('like_category/', views.LikeCategoryView.as_view(), name='like_category'),
    path('suggest/', views.CategorySuggestionView.as_view(), name='suggest'),
    path('search_add_page/', views.SearchAddPageView.as_view(), name='search_add_page'),
    path('search/', views.search_bar, name='search'),
 
]