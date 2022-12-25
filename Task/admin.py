from django.contrib import admin
from .models import *
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ['id','Title','Description','DueDate','Tags','Status','createdBy','timeStamp']

admin.site.register(TodoTask,TodoAdmin)
