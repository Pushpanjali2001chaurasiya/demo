from django.contrib import admin
from .models import *

@admin.register(students)

class studentAdmin(admin.ModelAdmin):
    list_display = ('id','Name','Age','Mobile','Email','Trade','Location')

# Register your models here.
