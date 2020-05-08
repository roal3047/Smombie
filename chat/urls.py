# chat/urls.py
from django.conf.urls import url, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'chat'

urlpatterns = [
    url(r'^$', views.chat.as_view(), name='chat_index'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)