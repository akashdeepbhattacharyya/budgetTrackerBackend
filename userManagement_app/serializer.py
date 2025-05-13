from rest_framework import serializers
from .models import UserManagement

class UserManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserManagement
        fields = ['email', 'password']