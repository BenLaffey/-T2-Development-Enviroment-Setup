from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello(request):
	return HttpResponse("Hello, world!")

def index(request):
	return render(request, 'index_hello.html')

def about(request):
	return render(request, 'about_hello.html')
