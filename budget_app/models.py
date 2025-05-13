from django.db import models
from userManagement_app.models import UserManagement as User
# Create your models here.
class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    month = models.CharField(max_length=7)  # Format: YYYY-MM
    total_budget = models.IntegerField(max_length=10)

    def __str__(self):
        return f'{self.user.userName} - {self.month}'