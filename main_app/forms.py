from django.db.models import fields
from django.forms import ModelForm
from .models import Usage

class UsageForm(ModelForm):
  # Meta object is needed for configuration
  class Meta:
    model = Usage
    fields = ["user", "date"]