from django.urls import path
from django.urls import include
from .views import LoginView

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    # path('register', RegisterView.as_view(), name='register'),
]
