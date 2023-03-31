from django.contrib import admin
from chat.models import Room, Message, Topic
# Register your models here.

admin.site.register(Topic)
admin.site.register(Room)
admin.site.register(Message)