from django.views.generic import (
  CreateView, 
  DeleteView, 
  DetailView, 
  ListView, 
  UpdateView,
)
from django.shortcuts import render, redirect
from .models import Tech, User
from .forms import UsageForm

# Create your views here.
def home(request):
  return render(request, "home.html")
def about(request):
  return render(request, "about.html")

def add_usage(request, tech_id):
  # instantiate a new form object using the key-value pairs from the post req
  form = UsageForm(request.POST)
  # check if the inputs are valid
  if form.is_valid():
    # create in-memory representation of the form object
    new_usage = form.save(commit=False)
    new_usage.tech_id = tech_id
    new_usage.save()
  return redirect("tech_detail", pk=tech_id)

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

class UsersList(ListView):
  model = User
class UsersDetail(DetailView):
  model = User
class UsersCreate(CreateView):
  model = User
  # create a form using all fields in Model
  fields = "__all__"
class UsersUpdate(UpdateView):
  model = User
class UsersDelete(DeleteView):
  model = User
  success_url = "/users/"