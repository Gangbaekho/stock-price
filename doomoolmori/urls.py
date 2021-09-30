from django.contrib import admin
from django.urls import path
from doomoolmori.views import DoomoolmoriAPI

urlpatterns = [
    path('', DoomoolmoriAPI.as_view()),
]