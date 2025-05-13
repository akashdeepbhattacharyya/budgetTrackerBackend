from django.contrib import admin
from .models import Transaction

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'type', 'category', 'date', 'description')
    list_filter = ('type', 'category', 'date')
    search_fields = ('user__username', 'category', 'description')
    ordering = ('-date',)
    date_hierarchy = 'date'

admin.site.register(Transaction, TransactionAdmin)
