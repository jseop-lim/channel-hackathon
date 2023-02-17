from rest_framework.generics import ListAPIView, RetrieveAPIView

from apis.chats.serializers import ChatRoomListSerializer, ChatRoomDetailSerializer
from apps.chats.models import ChatRoom


class ChatRoomListView(ListAPIView):
    serializer_class = ChatRoomListSerializer

    def get_queryset(self):
        return ChatRoom.objects.filter(
            user=self.request.user,
        )


class ChatRoomDetailView(RetrieveAPIView):
    serializer_class = ChatRoomDetailSerializer

    def get_queryset(self):
        return ChatRoom.objects.filter(
            user=self.request.user,
        )
