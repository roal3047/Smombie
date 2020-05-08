# chat/urls.py
from django.conf.urls import url
from django.urls import path,include
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'work'

urlpatterns = [
  path('', views.work, name='work'),
  path('insert/', views.check_post, name='work_insert'),
  path('index/', views.work, name='work_index'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)