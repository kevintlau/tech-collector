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
# class TechDetail(DetailView):
#   model = Tech
def tech_detail(request, pk):
  tech = Tech.objects.get(id=pk)
  # get the users that the tech doesn't belong to
  unlinked_users = User.objects.exclude(
    # exclude all users where user id is inside the tech's owner list
    id__in=tech.users.all().values_list("id")
  )
  # instantiate usage form to be rendered in template
  usage_form = UsageForm()
  return render(request, "tech/detail.html", { 
    "object": tech,
    "usage_form": usage_form,
    # add toys to be displayed in selector list
    "unlinked_users": unlinked_users,
  })
class TechCreate(CreateView):
  model = Tech
  # create a form using all fields in Model
  fields = [
    "name", "brand", "category", 
    "description", "release_year", 
    "purchase_date", "working"
  ]
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