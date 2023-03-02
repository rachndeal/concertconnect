from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	return HttpResponse("Here is the ConcertConnect home page.")

def concerts(request):
	return HttpResponse("Here's the upcoming concerts page.")