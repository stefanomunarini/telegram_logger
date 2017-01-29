from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from api.views import ChatMessageListView

urlpatterns = [
    url(r'^chat-messages/$', csrf_exempt(ChatMessageListView.as_view()), name='messages-for-chat'),
]
