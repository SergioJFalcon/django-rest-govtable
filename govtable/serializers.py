from rest_framework import serializers
from .models import GovTable

class GovTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = GovTable
        fields = ('Name', 'Address', 'ZipCode', 'Email')