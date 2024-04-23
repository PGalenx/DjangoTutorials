from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from quickstart.serializers import Userserializer, Groupserializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('date_joined')
    serializer_class = Userserializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = Groupserializer
    permission_classes = [permissions.IsAuthenticated]

