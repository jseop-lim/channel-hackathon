from django.urls import path

from apis.chats.views import ChatRoomListView, ChatRoomDetailView

urlpatterns = [
    path('', ChatRoomListView.as_view(), name='chat-room-list'),
    path('<int:pk>/', ChatRoomDetailView.as_view(), name='chat-room-detail'),
]
