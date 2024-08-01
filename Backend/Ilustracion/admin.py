from django.contrib import admin
from .models import Ilustracion

@admin.register(Ilustracion)

class IlustracionAdmin(admin.ModelAdmin):
    list_display = ('id','Description','Image')
