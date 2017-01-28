from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from api.views import ChatMessageListView
from bot.views import DispatcherView
from telegram_logger.credentials.private_keys import BOT_TOKEN

urlpatterns = [
    url(r'^chat-messages/$', ChatMessageListView.as_view(), name='chat-messages'),
]
