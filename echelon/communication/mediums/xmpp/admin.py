from django.contrib import admin
from models import XMPPMedium


class XMPPMediumAdmin(admin.ModelAdmin):
    pass

admin.site.register(XMPPMedium, XMPPMediumAdmin)
