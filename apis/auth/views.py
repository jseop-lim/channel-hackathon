from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apis.auth.serializers import LoginSignupResponseSerializer, LoginSignupRequestSerializer

User = get_user_model()


class LoginSignupView(APIView):
    permission_classes = [AllowAny]

    def put(self, request):
        input_serializer = LoginSignupRequestSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        try:
            user: User = User.objects.get(phone_number=input_serializer.validated_data['phone_number'])
        except User.DoesNotExist:
            user: User = User.objects.create_user(**input_serializer.validated_data)

        token, created = Token.objects.get_or_create(user=user)
        output_serializer = LoginSignupResponseSerializer(token)
        if created:
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        return Response(output_serializer.data, status=status.HTTP_200_OK)
