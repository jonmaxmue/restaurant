#from push_notifications.models import APNSDevice, GCMDevice
from django.dispatch import receiver
from django.db.models.signals import post_save, m2m_changed
from chat.models.Message import Message

import logging

logger = logging.getLogger(__name__)