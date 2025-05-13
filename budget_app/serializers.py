from rest_framework import serializers
from .models import Budget

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['id', 'user', 'month', 'total_budget']

class BudgetSummarySerializer(serializers.Serializer):
    month = serializers.CharField()
    total_budget = serializers.IntegerField(max_value=10)
    total_expenses = serializers.IntegerField(max_value=10)
    balance = serializers.IntegerField(max_value=10)
