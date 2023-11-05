from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models import UserActivation
from rest_framework.permissions import AllowAny
from utils.generate_random_secret_util import get_secret_key
from django.shortcuts import get_object_or_404


class AccountActivationAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, secret_key):
        try:
            """
            This api is used to activate user account
            Parameters:
                secret_key

            """

            secret_key = get_secret_key(secret_key)
            user_activation = get_object_or_404(
                UserActivation, activation_token=secret_key, user__is_active=False)

            if secret_key == user_activation.activation_token:
                if not user_activation.activated:
                    user_activation.activated = True
                    user_activation.user.is_active = True
                    user_activation.is_expired = True
                    user_activation.user.save()

                    user_activation.save()
                    return Response({"message": "Account activated successfully", "status": "200"}, status=status.HTTP_200_OK)
                return Response({"message": "Account already activated", "status": "400"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": str(e), "status": "500"}, status.HTTP_500_INTERNAL_SERVER_ERROR)
