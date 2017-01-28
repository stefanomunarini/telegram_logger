from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from bot.views import DispatcherView

urlpatterns = [
    url(r'^$', csrf_exempt(DispatcherView.as_view()), name='dispatcher'),
]
