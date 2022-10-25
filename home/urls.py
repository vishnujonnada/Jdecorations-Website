from unicodedata import name
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name="home"),
    path("home",views.index,name="home"),
    path("about",views.about,name="about"),
    path("contact",views.Contact,name="contact"),
    path("marriage",views.marriage,name="marriage"),
    path("backgrounds",views.backgrounds,name="backgrounds"),
    path("first_night",views.first_night,name="first_night"),
    path("haldhi",views.haldhi,name="haldhi"),
    path("house",views.house,name="house"),
    path("jd",views.jd,name="jd"),
    path("success",views.success,name="success")


]
