from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('',views.accounts),
    path('login',views.login),
    path('signup',views.signup),
    path('homepage',views.homepage),
    path('contact',views.contact),
    path('discussion',views.discussion),
    path('buy',views.buy),
    path('sell',views.sell),
    path('donate',views.donate),
]

