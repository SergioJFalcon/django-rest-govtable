from django.shortcuts import render
from rest_framework import viewsets
from .serializers import GovTableSerializer
from .models import GovTable

# Create your views here.

class GovTableView(viewsets.ModelViewSet):
    serializer_class = GovTableSerializer
    queryset = GovTable.objects.all()