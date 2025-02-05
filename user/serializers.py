# serializers.py
from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "email", "first_name", "last_name", "is_active", "is_staff"]

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Ajout du champ password

    class Meta:
        model = CustomUser  # Utilisation du modèle CustomUser
        fields = ["id", "email", "first_name", "last_name", "password", "is_active", "is_staff"]

    def create(self, validated_data):
        # Vérification si l'email existe déjà
        if CustomUser.objects.filter(email=validated_data["email"]).exists():
            raise serializers.ValidationError({"email": "Cet email est déjà utilisé."})

        user = CustomUser(
            email=validated_data["email"],
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
            is_active=validated_data.get("is_active", True),
            is_staff=validated_data.get("is_staff", False),
        )
        # Hash du mot de passe
        user.set_password(validated_data["password"])
        user.save()
        return user
