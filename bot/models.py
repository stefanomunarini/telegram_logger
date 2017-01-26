from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)


class Chat(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=31, null=False, blank=False)


class Message(models.Model):
    message_id = models.BigIntegerField()
    chat = models.ForeignKey(Chat, related_name='messages')
    user = models.ForeignKey(User, related_name='messages')
    date = models.DateTimeField()
    text = models.CharField(max_length=4095)

    class Meta:
        unique_together = (('chat', 'user', 'message_id'),)
