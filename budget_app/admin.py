
# Register your models here.
from django.contrib import admin
from .models import Budget

@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('user', 'month', 'total_budget')
    search_fields = ('user__username', 'month')
    list_filter = ('month',)
