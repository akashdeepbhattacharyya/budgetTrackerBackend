# userManagement_app/authentication.py
from rest_framework_simplejwt.authentication import JWTAuthentication
from userManagement_app.models import UserManagement

class CustomJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        user_id = validated_token.get('user_id')
        try:
            return UserManagement.objects.get(id=user_id)
        except UserManagement.DoesNotExist:
            return None
