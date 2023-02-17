from django.urls import include, path

urlpatterns = [
    path('auth/', include('apis.auth.urls')),
    path('chat-rooms/', include('apis.chats.urls')),
]
