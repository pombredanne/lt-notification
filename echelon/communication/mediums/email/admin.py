from django.contrib import admin
from models import EmailMedium


class EmailMediumAdmin(admin.ModelAdmin):
    pass

admin.site.register(EmailMedium, EmailMediumAdmin)
