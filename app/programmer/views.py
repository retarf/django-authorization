from django.shortcuts import render

# Create your views here.

from . import models, permissions, serializers
from rest_framework.viewsets import ModelViewSet


class ProgrammerViewSet(ModelViewSet):
    queryset = models.DataModel.objects.all()
    serializer_class = serializers.DataSerializer
    permission_classes = [permissions.AdminPermission]



