from django.contrib import admin

# Register your models here.
from .models import TeacherData, StatusData

admin.site.register(TeacherData)
admin.site.register(StatusData)

