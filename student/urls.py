from django.urls import path
from .views import *

urlpatterns = [
    path('students/', StudentView.as_view()),
    path('students/<str:pk>/', StudentView.as_view()),
]