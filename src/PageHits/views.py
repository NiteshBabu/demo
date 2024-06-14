from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request, *args, **kwargs):
    return HttpResponse("Hello, world. You're at the polls index.")