from django.contrib import admin
from .models import (
    Room,
    OnlineUser,
    RoomMessage,
    GroupRoom,
    ChatAttachment,
    GroupRoomMessage,
)

# Register your models here.


@admin.register(GroupRoom)
class WorkspaceRoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']


admin.site.register(ChatAttachment)


@admin.register(GroupRoomMessage)
class WorkspaceRoomMessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'room', 'profile',
                    'message', 'is_read', 'is_file', 'created_at']


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner', 'partner', 'created_at']


@admin.register(RoomMessage)
class RoomMessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'room', 'owner', 'message',
                    'is_read', 'is_file', 'created_at']


@admin.register(OnlineUser)
class OnlineUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile', 'channel_id', 'created_at']
