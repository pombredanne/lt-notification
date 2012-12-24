from django import forms

from communication.models import *
from django.contrib.contenttypes.models import ContentType


class CommunicationPreferenceForm(forms.ModelForm):
    medium = forms.ChoiceField(choices=[])

    def __init__(self, user=None, *args, **kwargs):
        '''
        limit the choice of owner to the currently logged in users hats
        '''
        super(CommunicationPreferenceForm, self).__init__(*args, **kwargs)
        if user:
            choices = [(a.pk, "[%s] %s" % (str(a._meta.verbose_name), a.name))
                       for a in
                       CommunicationMedium.objects.filter(user=user).select_subclasses()]
            self.fields["medium"].choices = choices

    def clean_medium(self):
        medium_pk = self.cleaned_data['medium']
        self.instance.medium = CommunicationMedium.objects.select_subclasses().get(pk=medium_pk)
        return medium_pk

    class Meta:
        model = CommunicationPreference
        exclude = ('user', 'medium_content_type', 'medium_object_id')
