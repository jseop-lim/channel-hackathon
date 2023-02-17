from rest_framework import serializers


class LoginSignupRequestSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=20)
    email = serializers.EmailField(max_length=255)


class LoginSignupResponseSerializer(serializers.Serializer):
    token = serializers.CharField(source='key', max_length=255)
