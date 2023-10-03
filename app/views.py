# app/views.py
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .models import UserBadge
from .serializers import BadgeSerializer
# Vue  pour afficher la liste des modèles 3D
class BadgeListAPIView(generics.ListAPIView):
    queryset = UserBadge.objects.all()
    serializer_class = BadgeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return UserBadge.objects.filter(user=user)
