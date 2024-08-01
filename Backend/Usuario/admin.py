from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'lasName', 'userName', 'email', 'password', 'sex', 'telephone', 'ilustracion']