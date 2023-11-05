from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    GroupRoomSerializer,
)
from .models import (
    GroupRoom,
)


class GroupRoomViewSet(viewsets.ModelViewSet):
    queryset = GroupRoom.objects.all()
    serializer_class = GroupRoomSerializer

    def get_queryset(self):
        user = self.request.user
        return GroupRoom.objects.filter(profile=user.profile)
