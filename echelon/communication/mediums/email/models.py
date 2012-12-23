from communication.models import CommunicationMedium
from django.db import models


class EmailMedium(CommunicationMedium):
    from_address = models.EmailField(default="notifier@lateral-thoughts.com")
    to_address = models.EmailField()
    subject_prefix = models.CharField(max_length=50, blank=True, default="[Prefix]")

    def summary(self):
    	return "Email -> %s" % (self.to_address) 

    def tooltip(self):
    	return "Email from '%s' to '%s' prefixing subject with '%s'" % (self.from_address, self.to_address, self.subject_prefix)