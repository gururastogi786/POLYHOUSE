from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from polls import views

urlpatterns = [

    path("", views.index, name='polls'),
    path("anmol/", views.about, name='about'),
    path("services/", views.services, name='services'),
    path("contact/", views.contact, name='contact'),
    path("signup/", views.signup, name='signup'),

]