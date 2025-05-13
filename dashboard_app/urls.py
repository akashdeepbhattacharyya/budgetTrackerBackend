from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DashboardView


urlpatterns = [
   path('', DashboardView.as_view(), name='dashboard'),

]
