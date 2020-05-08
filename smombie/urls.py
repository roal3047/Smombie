from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls import url

urlpatterns = [
  path('', views.index, name='index'),
  path('work', views.work, name='work'),
  path('chat_index', views.chat_index, name='chat_index'),
  url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
 
]