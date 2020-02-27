from django.urls import  path, include
from .views import *


urlpatterns = [

    path('index/', index),
    path('about/', about),
    path('listpic/', listpic),
    path('newslistpic/', newslistpic),
    path('test/', test),
    path('add/', add),
    path('article/', article),
    path('register/', register),
    path('register_ajax/', register_ajax),
    path('ajax_get/', ajax_get),
    path('ajax_post/', ajax_post),
    path('author/', authors),
]