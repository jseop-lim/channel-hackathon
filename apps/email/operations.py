from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from apps.chats.models import DailyChat, ChatRoom

User = get_user_model()


def send_mail_from_chat_room(
    chat_room_id: int,
):
    chat_room = ChatRoom.objects.get(id=chat_room_id)
    send_mail(
        subject=chat_room.name,
        message=''.join([f'- {daily_chat.summury_text}\n' for daily_chat in chat_room.daily_chats.all()]),
        from_email='jseoplim2@gmail.com',
        recipient_list=[chat_room.user.email],
        fail_silently=False,
    )
