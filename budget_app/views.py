from .models import Budget
from .serializers import BudgetSummarySerializer
from datetime import datetime
from transaction_app.models import Transaction
from django.db import models
from rest_framework import permissions, status, views, response

class CurrentMonthBudgetView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, year_month):
        user = request.user
        try:
            date_obj = datetime.strptime(year_month, '%Y-%m')
        except ValueError:
            return response.Response({'error': 'Invalid date format. Use YYYY-MM'}, status=400)

        print(date_obj)
        month_str = date_obj.strftime('%Y-%m')

        # Try to get the budget
        try:
            budget = Budget.objects.get(user=user, month=month_str)
            total_expenses = Transaction.objects.filter(
                user=user,
                type="expense",
                date__year=date_obj.year,
                date__month=date_obj.month
            ).aggregate(total=models.Sum('amount'))['total'] or 0

            data = {
                'month': month_str,
                'total_budget': budget.total_budget,
                'total_expenses': total_expenses,
                'balance': budget.total_budget - total_expenses
            }

            return response.Response(BudgetSummarySerializer(data).data)

        except Budget.DoesNotExist:
            # No budget found — return empty object
            return response.Response({})


class AddBudgetView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user
        date_str = request.data.get('date')  # e.g. "2025-05"
        total_budget = request.data.get('budget')  # e.g. 10

        if not date_str or not total_budget:
            return response.Response(
                {'error': 'Both "date" and "budget" are required.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            date_obj = datetime.strptime(date_str, '%Y-%m')
        except ValueError:
            return response.Response({'error': 'Invalid date format. Use YYYY-MM'}, status=400)

        try:
            total_budget = int(total_budget)
        except ValueError:
            return response.Response({'error': 'Budget must be a number.'}, status=400)
        print(date_obj)
        month_str = date_obj.strftime('%Y-%m')
        print(month_str)
        # Save or update the budget
        budget, created = Budget.objects.update_or_create(
            user=user,
            month=month_str,
            defaults={'total_budget': total_budget}
        )

        return response.Response({
            'message': 'Budget added' if created else 'Budget updated',
            'month': month_str,
            'total_budget': budget.total_budget
        }, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)