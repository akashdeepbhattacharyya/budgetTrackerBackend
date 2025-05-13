from django.db import models
from userManagement_app.models import UserManagement
class Transaction(models.Model):
    TYPE_CHOICES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]
    CATEGORY_CHOICES = [
        ('salary', 'Salary'),
        ('groceries', 'Groceries'),
        ('entertainment', 'Entertainment'),
        ('other', 'Other'),
    ]
    
    # Replace direct import with settings.AUTH_USER_MODEL
    user = models.ForeignKey(
        UserManagement,
        on_delete=models.CASCADE,
        related_name='transactions'
    )
    amount = models.IntegerField(max_length=10)
    type = models.CharField(max_length=7, choices=TYPE_CHOICES)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.userName} - {self.type} - {self.amount}"