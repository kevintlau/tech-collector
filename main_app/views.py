from main_app.models import Tech
from django.views.generic import (
  CreateView, 
  DeleteView, 
  DetailView, 
  ListView, 
  UpdateView,
)
from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, "home.html")

def about(request):
  return render(request, "about.html")

class TechList(ListView):
  model = Tech

class TechDetail(DetailView):
  model = Tech

class TechCreate(CreateView):
  model = Tech
  # create a form using all fields in Model
  fields = "__all__"

class TechUpdate(UpdateView):
  model = Tech
  fields = ["name", "category", "description", "working"]

class TechDelete(DeleteView):
  model = Tech
  success_url = "/tech/"