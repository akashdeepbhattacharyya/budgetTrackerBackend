
# finance/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from datetime import date
from django.db.models import Sum
from transaction_app.models import Transaction
from budget_app.models import Budget

class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        transactions = Transaction.objects.filter(user=user)
        income = transactions.filter(type='income').aggregate(total=Sum('amount'))['total'] or 0
        expenses = transactions.filter(type='expense').aggregate(total=Sum('amount'))['total'] or 0
        balance = income - expenses

        budget = Budget.objects.filter(user=user).first()
        budget_amount = budget.total_budget if budget else 0

        return Response({
            'total_income': income,
            'total_expenses': expenses,
            'balance': balance,
            'monthly_budget': budget_amount,
            'budget_remaining': budget_amount - expenses
        })
