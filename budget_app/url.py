from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CurrentMonthBudgetView, AddBudgetView


urlpatterns = [
    path('add', AddBudgetView.as_view(), name='budget-add'),
    path('<str:year_month>', CurrentMonthBudgetView.as_view(), name='budget-list'),
]
