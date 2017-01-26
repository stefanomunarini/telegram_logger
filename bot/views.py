from queue import Queue

from django.http import JsonResponse
from django.views import View
# import the logging library
import logging

# Get an instance of a logger
from bot.models import Chat, User, Message

logger = logging.getLogger(__name__)


class DispatcherView(View):
    def dispatch(self, request, *args, **kwargs):
        import ipdb; ipdb.set_trace()
        print('ciao')
        data = request.body
        message = data.get('message')
        chat = message.get('chat')
        user = message.get('from')

        if message.get('text') == '/stop':
            logger.error('/stop chat_id={}'.format(chat.get('id')))
        elif message.get('text') == '/stop':
            logger.error('/start chat_id={}'.format(chat.get('id')))
        else:
            user_obj = User.objects.get_or_create(id=user.get('id'))
            user_obj.first_name = user.get('first_name')
            user_obj.last_name = user.get('last_name')
            user_obj.username = user.get('username')

            chat_obj = Chat.objects.get_or_create(id=chat.get('id'))
            chat_obj.title = chat.get('title')
            chat_obj.type = chat.get('type')

            message_obj = Message.objects.get_or_create(id=message.get('message_id'))
            message_obj.chat = chat_obj
            message_obj.user = user_obj
            message_obj.date = message.get('date')
            message_obj.text = message.get('text')

        return JsonResponse(data={'user': user_obj.__dict__,
                                  'chat': chat_obj.__dict__,
                                  'message': message_obj.__dict__,
                                  }, status=200)
