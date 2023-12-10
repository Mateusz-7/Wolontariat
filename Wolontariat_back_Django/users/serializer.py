from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'surname', 'password', 'email', 'phone', 'shirt_size', 'role']
