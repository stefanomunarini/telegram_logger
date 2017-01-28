from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from bot.models import Message


class ChatMessageListView(ListView):
    model = Message

    def dispatch(self, request, *args, **kwargs):
        super(ChatMessageListView, self).dispatch(request, *args, **kwargs)
        return HttpResponse(serializers.serialize('json', self.get_queryset()), status=200)
