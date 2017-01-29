"""telegram_logger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include

from api import urls as api_urls
from bot import urls as bot_urls
from search import urls as search_urls
from telegram_logger.credentials.private_keys import BOT_TOKEN

urlpatterns = [
    url(r'^bot/{}'.format(BOT_TOKEN), include(bot_urls, namespace='bot')),
    url(r'^bot/{}/api/v1/'.format(BOT_TOKEN), include(api_urls, namespace='api')),
    url(r'^search/', include(search_urls, namespace='search')),
]
