from rest_framework import serializers
from .models import CustomClient

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomClient
        fields = '__all__'