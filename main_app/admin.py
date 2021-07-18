from django.contrib import admin

# Register your models here.
from .models import Tech, User, Usage

admin.site.register(Tech)
admin.site.register(User)
admin.site.register(Usage)