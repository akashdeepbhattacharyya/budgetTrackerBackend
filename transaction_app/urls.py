from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionViewSet


urlpatterns = [
    path('list', TransactionViewSet.as_view({'get': 'list'}), name='transaction-list'),
    path('add', TransactionViewSet.as_view({'post': 'create'}), name='transaction-add'),
    path('update/<int:pk>', TransactionViewSet.as_view({'put': 'update'}), name='transaction-update'),
    path('delete/<int:pk>', TransactionViewSet.as_view({'delete': 'destroy'}), name='transaction-delete'),

]
