from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name", "role")
        read_only_fields = ("id", "role")


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=User.ROLE_CHOICES, default="student")

    class Meta:
        model = User
        fields = ("username", "email", "password", "first_name", "last_name", "role")

    def create(self, validated_data):
        role = validated_data.pop("role", "student")
        user = User.objects.create_user(**validated_data)
        user.role = role
        user.save()
        return user
