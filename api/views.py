from django.http import JsonResponse
from django.views.generic import ListView

from bot.models import Message


class ChatMessageListView(ListView):
    model = Message

    def dispatch(self, request, *args, **kwargs):
        super(ChatMessageListView, self).dispatch(request, *args, **kwargs)
        return JsonResponse(data=self.serialize_messages(), status=200)

    def serialize_messages(self):
        return {
            'messages': [
                {
                    "message_id": message.message_id,
                    "chat": message.chat.id,
                    "user": message.user.id,
                    "date": message.date,
                    "text": message.text
                }
                for message
                in self.get_queryset()
            ]
        }
