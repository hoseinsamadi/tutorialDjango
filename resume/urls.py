from django.urls import path
from resume.views import *

urlpatterns = [
    path('home-test',home_test),
    path('about-test',about_test),
    path('contact-test',contact_test),
]
