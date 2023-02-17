from django.core.mail import send_mail

from apps.chats.models import DailyChat


class EmailService:

    def send_mail_from_daily_chat(
        self,
        daily_chat: DailyChat,
    ):
        send_mail(
            subject=daily_chat.chat_room.name,
            message=daily_chat.summary_text,
            from_email='jseoplim2@gmail.com',
            recipient_list=[daily_chat.chat_room.user.email],
            fail_silently=False,
        )
