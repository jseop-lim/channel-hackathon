from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class ChatRoom(models.Model):
    name = models.CharField(
        '이름',
        max_length=255,
    )
    user = models.ForeignKey(
        User,
        verbose_name='사용자',
        on_delete=models.CASCADE,
        related_name='chat_rooms',
    )
    created_at = models.DateTimeField(
        '생성일시',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = '채팅방'
        verbose_name_plural = '채팅방'
        ordering = ('-created_at',)


class DailyChat(models.Model):

    class Level(models.IntegerChoices):
        NONE = 0, '상관없음'
        EASE = 1, '고등학생 이하'
        NORMAL = 2, '대학생'
        HARD = 3, '직장인'

    raw_text = models.TextField(
        '원시 텍스트',
        blank=True,
    )
    summary_text = models.TextField(
        '요약 텍스트',
        blank=True,
    )
    level = models.IntegerField(
        '수준',
        choices=Level.choices,
    )
    created_at = models.DateTimeField(
        '생성일시',
        auto_now_add=True,
    )
    chat_room = models.ForeignKey(
        ChatRoom,
        verbose_name='채팅방',
        on_delete=models.CASCADE,
        related_name='daily_chats',
    )

    class Meta:
        verbose_name = '일일 채팅'
        verbose_name_plural = '일일 채팅'
        ordering = ('-created_at',)
