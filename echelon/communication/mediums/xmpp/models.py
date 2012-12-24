from communication.models import CommunicationMedium
from django.db import models


class XMPPMedium(CommunicationMedium):
    class Meta:
        verbose_name = "XMPP based"
