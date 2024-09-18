from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from .models import notification
from .serializers import notificationSerializer
from rest_framework import generics 

class notificationListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = notificationSerializer

    def get_queryset(self):
        return notification.objects.filter(recipient=self.request.user).order_by('-timestamp')
