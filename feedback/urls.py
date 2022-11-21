from django.contrib import admin
from django.urls import path
from . import views
from .views import index, done

urlpatterns = [
    path('done', done),
    path('', views.index, name="index"),

]
