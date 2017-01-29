from dateutil import parser
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
        user_id = None
        chat_id = None
        date = None
        if self.request.method == 'POST':
            user_id = self.request.POST.get('user_id')
            chat_id = self.request.POST.get('chat_id')
            date = self.request.POST.get('date')
        if user_id:
            self.queryset = self.queryset.filter(user=get_object_or_404(User, id=user_id))
        if date:
            self.queryset = self.queryset.filter(date__gte=parser.parse(date))
        if chat_id:
            return self.queryset.filter(chat=get_object_or_404(Chat, id=chat_id))
        return self.model.objects.none()

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
