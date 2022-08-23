from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User
# Register your models here.

@admin.register(User)
class UserAdmin(BaseUserAdmin):
      fieldsets= (
      (None, {'fields': ('username', 'password', 'email')}),
      ('Datos del usuario', {'fields': ('first_name', 'last_name', 'country', 'facebook', 'instagram', 'picture')}),
      ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
  )

