from core.serializers import CreateUserSerializer
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework import status
from utils.generate_random_secret_util import create_secret_key
from utils.threads.email_thread import send_mail
from django.conf import settings
from datetime import date
from core.models import UserActivation
from django.db import transaction


User = get_user_model()
email = settings.EMAIL_HOST_USER
react_domain = settings.REACT_DOMAIN


class RegistrationView(APIView):
    """REgister and login api instant """

    permission_classes = (permissions.AllowAny,)
    serializer_class = CreateUserSerializer

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        try:
            serializer = CreateUserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            instance = serializer.instance
            secret_key = create_secret_key(100, instance)

            key = {
                'username': instance.username,
                'button': react_domain+'auth/account-verified/'+secret_key,
                'year': date.today().year
            }

            subject = "Verify Your Account"
            template_name = "auth/new_userRegister.html"
            recipient = [request.data['email']]

            send_mail(subject=subject, html_content=template_name,
                      recipient_list=recipient, key=key)

            return Response({
                "message": "User created successfully. Check your email for verification"
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                "message": str(e)
            }, status=status.HTTP_418_IM_A_TEAPOT)
