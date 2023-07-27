from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ('email', 'is_superuser', 'is_staff')


admin.site.register(CustomUser, CustomUserAdmin)
