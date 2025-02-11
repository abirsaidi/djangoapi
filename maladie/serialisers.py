from rest_framework import serializers
from .models import Maladies

class MaladieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maladies
        fields = '__all__'
