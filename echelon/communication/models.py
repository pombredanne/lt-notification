from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User
from communication.fields import TimedeltaField
from django.db import models


class CommunicationFrequency(models.Model):
    name = models.CharField(max_length=100)
    frequency = TimedeltaField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    @property
    def description(self):
        return "Every hour a summary will be sent"

    def __unicode__(self):
        return self.name


class CommunicationPreference(models.Model):
    user = models.ForeignKey(User, related_name="preferences")
    # generic relationship to all the possible medium
    medium_content_type = models.ForeignKey(ContentType)
    medium_object_id = models.PositiveIntegerField()
    medium = generic.GenericForeignKey('medium_content_type',
                                       'medium_object_id')
    frequency = models.ForeignKey(CommunicationFrequency)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class CommunicationMedium(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_private = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True
