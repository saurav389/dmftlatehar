from django.contrib import admin
from .models import HighPriority,LowPriority
# Register your models here.
mymodels = [HighPriority,LowPriority]
admin.site.register(mymodels)