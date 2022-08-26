from django.contrib import admin
from adminapp.models import Person, Role
# Create your models here.
admin.site.register(Person)
admin.site.register(Role)