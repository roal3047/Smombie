from django.shortcuts import render, redirect
from django.views import generic
from .models import SmombieDb
from .forms import WorkForm

# Create your views here.
class work(generic.TemplateView):
  def get(self, request, *args, **kwargs):
      template_name = 'work/work_index.html'
      SmombieDb_work = SmombieDb.objects.all()
      return render(request, template_name, {"SmombieDb_work": SmombieDb_work})

def check_post(request):
  template_name = 'work/work_success.html'
  if request.method == "POST":
    form = WorkForm(request.POST)
    if form.is_valid():
       work_save = form.save(commit=False)
       work_save.work_save()
       message = "업무를 추가하였습니다."
       return render(request, template_name, {"message" : message})
  else:
      template_name = 'work/work_insert.html'
      form = WorkForm
      return render(request, template_name, {"form" : form})