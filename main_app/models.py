from django.db import models
from django.urls import reverse

# Create your models here.
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
