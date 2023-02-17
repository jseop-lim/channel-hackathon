from rest_framework import serializers

from apps.chats.models import DailyChat


class ChatRoomListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    created_at = serializers.DateTimeField()


class DailyChatSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    summary_text = serializers.CharField()
    level = serializers.ChoiceField(choices=DailyChat.Level.choices)
    created_at = serializers.DateTimeField()


class ChatRoomDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    created_at = serializers.DateTimeField()
    daily_chats = DailyChatSerializer(many=True)
