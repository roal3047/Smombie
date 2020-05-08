from django.shortcuts import render, redirect
from django.views import generic
from django.utils.safestring import mark_safe
import json

# Create your views here.
class chat(generic.TemplateView):
  def get(self, request, *args, **kwargs):
      template_name = 'chat/chat_index.html'
      return render(request, template_name)

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })