from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserManagement
from django.contrib.auth.hashers import check_password, make_password
from rest_framework_simplejwt.tokens import RefreshToken

class LoginView(APIView):
    def post(self, request):
        userName = request.data.get('userName')
        password = request.data.get('password')
        try:
            user = UserManagement.objects.get(userName=userName)
            print(user.password, password)
            print(check_password(password, user.password))
            if check_password(password, user.password):
                refresh = RefreshToken.for_user(user)
                return Response({"message": "Login successful", "refresh": str(refresh),
    "access": str(refresh.access_token), "userName": userName, "email": user.email}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        except UserManagement.DoesNotExist:
            return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class RegisterView(APIView):
    def post(self, request):
        userName = request.data.get('userName')
        email = request.data.get('email')
        password = request.data.get('password')

        if not userName or not password or not email:
            return Response({"message": "Username, email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        if UserManagement.objects.filter(userName=userName).exists():
            return Response({"message": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = UserManagement.objects.create(
                userName=userName,
                email=email,
                password=password  # Hash the password before saving
            )

            return Response({
                "message": "Registration successful",
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message": "Registration failed", "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)