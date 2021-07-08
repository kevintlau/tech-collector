from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name="home"),
  path("about/", views.about, name="about"),

  path("tech/", views.TechList.as_view(), name="tech_index"),
  path("tech/<int:pk>/", views.TechDetail.as_view(), name="tech_detail"),
  path("tech/create/", views.TechCreate.as_view(), name="tech_create"),
  path("tech/<int:pk>/update", views.TechUpdate.as_view(), name="tech_update"),
  path("tech/<int:pk>/delete", views.TechDelete.as_view(), name="tech_delete"),
]