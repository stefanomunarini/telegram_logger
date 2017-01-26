from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from bot.views import DispatcherView
from telegram_logger.credentials.private_keys import BOT_TOKEN

urlpatterns = [
    url(r'^{}$'.format(BOT_TOKEN), csrf_exempt(DispatcherView.as_view()), name='dispatcher'),
]
