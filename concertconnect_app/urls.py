from django.urls import path
from concertconnect_app import views

app_name = 'concertconnect_app'

urlpatterns = [
	path('', views.index, name='index'),
	path('concerts/', views.concerts, name='concerts'),
	path('signup/', views.signup, name='signup'),
	path('login/', views.login, name='login'),
	path('venue/', views.venue, name='venue'),
	path('search/', views.search, name='search'),
]

##still need to add /userprofile etc (/addreview)