from django.urls import path
from rest_framework.routers import DefaultRouter
from .api import (
    CreateRoomView,
    ListRoomsView,
    ChatAttachmentView,
    RoomPreviousChatView,
    OnlineStatusUpdateView,
    GroupActivityPreviousChatView,
)
from .views import GroupRoomViewSet

router = DefaultRouter()

router.register('group-room', GroupRoomViewSet, basename='group-room')

urlpatterns = [
    path('create-room/', CreateRoomView.as_view(), name='create_room'),
    path('get-all-rooms/', ListRoomsView.as_view(), name='list_rooms'),
    path('create-attachment/', ChatAttachmentView.as_view(),
         name='create_attachment'),
    path('update-online-status/', OnlineStatusUpdateView.as_view(),
         name='update_online_status'),
    path('get-room-previous-chat/<int:id>/',
         RoomPreviousChatView.as_view(), name='room_prev_chat'),
    path('get-group-activity-previous-chat/',
         GroupActivityPreviousChatView.as_view(), name='ws_prev_chat'),
]
