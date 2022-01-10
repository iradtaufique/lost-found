from django.db import models
from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from documents.models import Idcollection
from rest_framework import serializers
# from .models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class IdSerializer(ModelSerializer):
    class Meta:
        model = Idcollection
        fields = '__all__'


class UserSerializer(ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ('phone', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['phone'], validated_data['first_name'], validated_data['last_name'], validated_data['password'])

        return user
