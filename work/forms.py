from django import forms
from .models import SmombieDb

class WorkForm(forms.ModelForm):
  class Meta:
      model = SmombieDb
      fields = ('title', 'content', 'end_date')