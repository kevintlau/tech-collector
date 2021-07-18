from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name="home"),
  path("about/", views.about, name="about"),

  path("tech/", views.TechList.as_view(), name="tech_index"),
  path("tech/<int:pk>/add_usage", views.add_usage, name="add_usage"),
  path("tech/<int:pk>/", views.tech_detail, name="tech_detail"),
  path("tech/create/", views.TechCreate.as_view(), name="tech_create"),
  path("tech/<int:pk>/update", views.TechUpdate.as_view(), name="tech_update"),
  path("tech/<int:pk>/delete", views.TechDelete.as_view(), name="tech_delete"),

  path("users/", views.UsersList.as_view(), name="users_index"),
  path("users/<int:pk>/", views.UsersDetail.as_view(), name="users_detail"),
  path("users/create/", views.UsersCreate.as_view(), name="users_create"),
  path("users/<int:pk>/update", views.UsersUpdate.as_view(), name="users_update"),
  path("users/<int:pk>/delete", views.UsersDelete.as_view(), name="users_delete"),
]