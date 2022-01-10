from rest_framework import generics, serializers, validators
from rest_framework.utils import model_meta
# from documents.models import User
from rest_framework. response import Response
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ['phone', 'first_name', 'last_name', 'password']

        def validate(self, attrs):
            phone = attrs.get('phone', '')
            username = attrs.get('username', '')
            if not phone.alnum():
                raise serializers.ValidationError(
                    "only contains alpha numeric numbers")
            return attrs

        def create(self, validated_data):
            return User.objects.create_user(validated_data)
