from django.db import models
from django.urls import reverse

# Create your models here.

# User Model
class User(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse("users_detail", kwargs={ "pk": self.id })


# Tech Model
class Tech(models.Model):
  class Meta:
    ordering = ["name"] # order alphabetically

  name = models.CharField(max_length=50)
  brand = models.CharField(max_length=50)
  category = models.CharField(max_length=20)
  description = models.TextField(max_length=250)
  release_year = models.IntegerField("release year")
  purchase_date = models.DateField("purchase date")
  working = models.BooleanField(default=True)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse("tech_detail", kwargs={ "pk": self.id })


# Usage Model
class Usage(models.Model):
  class Meta:
    ordering = ["-date"]

  date = models.DateField("last used")
  tech = models.ForeignKey(Tech, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.user} on {self.date}"
