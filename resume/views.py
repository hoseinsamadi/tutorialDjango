from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse

def home_test(request):
    return HttpResponse('<h1>Home</h1>')


def about_test(request):
    return HttpResponse('<h1>About</h1>')

def contact_test(request):
    return HttpResponse('<h1>Contact US</h1>')


