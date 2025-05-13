from django.contrib import admin
from .models import UserManagement
# Register your models here.
@admin.register(UserManagement)
class UserManagementAdmin(admin.ModelAdmin):
    list_display = ('email',)