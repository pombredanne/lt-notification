from django.conf.urls import patterns, include, url
from django.contrib import admin

from communication.forms import CommunicationPreferenceForm

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'communication.views.index', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls')),
    url(r'', include('social_auth.urls')),
    url(r'^preference/(?P<object_id>\d+)/$',
        'communication.views.change',
        name="pref_detail"),
)
