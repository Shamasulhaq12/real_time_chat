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

    def create(self, request, *args, **kwargs):
        serializer = GroupRoomSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(group_creator=request.user.profile)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.group_admin.filters(user=request.user).exists() or instance.group_moderator.filters(user=request.user).exists():
            serializer = self.get_serializer(
                instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'message': "you are not be able to do..."}, status=status.HTTP_401_UNAUTHORIZED)
