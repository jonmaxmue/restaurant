from django.contrib.auth import get_user_model
from channels.db import database_sync_to_async
from chat.models.Chat import Chat
from chat.models.Contact import Contact
from chat.models.Message import Message

@database_sync_to_async
def create_user(
    *,
    username='memberA',
    password='pAssw0rd!',
    phone_number='017682828282',
    email='member@bla.de',
):
    user = get_user_model().objects.create_user(
        username=username,
        password=password,
        phone_number=phone_number,
        email=email
    )
    user.save()
    return user