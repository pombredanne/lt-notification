from django.contrib import admin
from communication.models import *


class CommunicationPreferenceAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'modified_at')

admin.site.register(CommunicationPreference, CommunicationPreferenceAdmin)


class CommunicationFrequencyAdmin(admin.ModelAdmin):
    pass

admin.site.register(CommunicationFrequency, CommunicationFrequencyAdmin)
