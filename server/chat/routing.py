from .consumers import (
    ChatUpdateConsumers,
    OnlineStatusConsumer,
    DashboardChatConsumer,
    UserOnlineStatusConsumer,
    WorkspaceActivityAsyncConsumer,
    CustomSendOfferStatusChangeConsumer,
)
from django.urls import path


websocket_urlpatterns = [

    path('api/workspace/activity/chat/',
         WorkspaceActivityAsyncConsumer.as_asgi()),
    path('api/dashboard/chat/', DashboardChatConsumer.as_asgi()),
    path('api/online/status/', OnlineStatusConsumer.as_asgi()),
    path('api/chat/update/', ChatUpdateConsumers.as_asgi()),
    path('api/custom/send/offer/status/change/',
         CustomSendOfferStatusChangeConsumer.as_asgi()),
    path('api/user/online/status/', UserOnlineStatusConsumer.as_asgi()),
]
