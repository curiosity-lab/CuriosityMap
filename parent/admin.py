from django.contrib import admin

# Register your models here.
from .models import ChildData, ParentData

admin.site.register(ChildData)
admin.site.register(ParentData)
