import json
import logging
from datetime import datetime

from django.http import JsonResponse
from django.views import View

from bot.models import Chat, User, Message

logger = logging.getLogger(__name__)


def set_logging_state(chat_obj, active):
    chat_obj.logging = active
    chat_obj.save()


class DispatcherView(View):
    chat = None

    def dispatch(self, request, *args, **kwargs):
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode.rstrip('\n'))
        message = data.get('message')
        user = message.get('from')
        self.chat = message.get('chat')

        chat_obj, _ = Chat.objects.get_or_create(id=self.chat.get('id'))
        chat_obj.title = self.chat.get('title')
        chat_obj.type = self.chat.get('type')

        if message['text'] == '/stop':
            set_logging_state(chat_obj, active=False)
            return JsonResponse(data=self.create_response(response_message='Logging disabled.'), status=200)
        elif message['text'] == '/start':
            set_logging_state(chat_obj, active=True)
            return JsonResponse(data=self.create_response(response_message='Logging enabled.'), status=200)
        else:
            user_obj, _ = User.objects.get_or_create(id=user.get('id'))
            user_obj.first_name = user.get('first_name')
            user_obj.last_name = user.get('last_name')
            user_obj.username = user.get('username')
            user_obj.save()

            if chat_obj.logging:
                message_obj, _ = Message.objects.get_or_create(message_id=message.get('message_id'),
                                                               chat=chat_obj,
                                                               user=user_obj)
                message_obj.data = datetime.fromtimestamp(message.get('date'))
                message_obj.text = message.get('text')
                message_obj.save()

        return JsonResponse(data={}, status=200)

    def create_response(self, response_message):
        return {
            'chat_id': self.chat.get('id'),
            'text': response_message
        }

