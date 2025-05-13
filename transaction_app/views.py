from rest_framework import serializers, permissions,status
from rest_framework.exceptions import ValidationError
from .models import Transaction
from userManagement_app.models import UserManagement
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .serializers import TransactionSerializer
from rest_framework.response import Response

class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['type', 'category', 'date']
    search_fields = ['description', 'category']
    ordering_fields = ['amount', 'date']

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            try:
                user_management_instance = UserManagement.objects.get(userName=user)
            except UserManagement.DoesNotExist:
                return Transaction.objects.none()  # Return empty queryset if user doesn't exist
            return Transaction.objects.filter(user=user_management_instance)
        return Transaction.objects.none()  # Return empty queryset if not authenticated

    def perform_create(self, serializer):
        # Save the transaction with the current user
        serializer.save(user=self.request.user)
    def update(self, request, pk=None):
        print("Transaction update triggered")
        try:
            transaction = self.get_queryset().get(pk=pk)
        except Transaction.DoesNotExist:
            raise ValidationError("Transaction not found.")

        serializer = TransactionSerializer(transaction, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, pk=None):
        try:
            transaction = self.get_queryset().get(pk=pk)
        except Transaction.DoesNotExist:
            raise ValidationError("Transaction not found.")

        transaction.delete()
        return Response({"detail": "Transaction deleted successfully."}, status=status.HTTP_204_NO_CONTENT)