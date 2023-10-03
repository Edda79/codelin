# app/serializers.py
from rest_framework import serializers
from .models import UserBadge, Badge

class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBadge
        fields = ('badge', 'earned_at')
