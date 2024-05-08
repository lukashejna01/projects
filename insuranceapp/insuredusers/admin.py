from django.contrib import admin
from .models import InsuredUser, Address

# Register your models here.
admin.site.register(InsuredUser)
admin.site.register(Address)