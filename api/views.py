from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from bot.models import Message, Chat, User


class ChatMessageListView(ListView):
    model = Message

    def dispatch(self, request, *args, **kwargs):
        super(ChatMessageListView, self).dispatch(request, *args, **kwargs)
        return JsonResponse(data=self.serialize_messages(), status=200)

    def get_queryset(self):
        self.queryset = super(ChatMessageListView, self).get_queryset()
        if self.kwargs.get('user_id'):
            self.queryset.filter(user=get_object_or_404(User, id=self.kwargs.get('user_id')))
        return self.queryset.filter(chat=get_object_or_404(Chat, id=self.kwargs.get('chat_id')))

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
