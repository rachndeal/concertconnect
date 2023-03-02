from django.urls import path
from concertconnect_app import views

app_name = 'concertconnect_app'

urlpatterns = [
	path('', views.index, name='index'),
	path('concerts/', concerts.index, name='concerts'),
]