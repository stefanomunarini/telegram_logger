from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from api.views import ChatMessageListView

urlpatterns = [
    url(r'^chat-messages/$', csrf_exempt(ChatMessageListView.as_view()), name='messages-for-chat'),
    url(r'^chat-messages/(?P<chat_id>[0-9]+)/$', ChatMessageListView.as_view(), name='chat-messages'),
    url(r'^chat-messages/(?P<chat_id>[0-9]+)/(?P<user_id>.*[0-9]+)/$', ChatMessageListView.as_view(), name='chat-messages'),
]
