# app/urls.py
from django.urls import path
from .views import BadgeListAPIView

urlpatterns = [
    path('badges/', BadgeListAPIView.as_view(), name='badge-list'),
]
