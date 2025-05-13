from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserManagement
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken

class LoginView(APIView):
    def post(self, request):
        print(self.request.data)
        userName = request.data.get('userName')
        password = request.data.get('password')
        try:
            user = UserManagement.objects.get(userName=userName)
            if check_password(password, user.password):
                refresh = RefreshToken.for_user(user)
                return Response({"message": "Login successful", "refresh": str(refresh),
    "access": str(refresh.access_token), "userName": userName}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        except UserManagement.DoesNotExist:
            return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
