from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from communication.forms import CommunicationPreferenceForm
from communication.models import CommunicationPreference


@login_required
def index(request,
          template_name="index.html"):
    """Homepage"""
    return render(request, template_name, {'user': request.user})


@login_required
def change(request,
           object_id,
           template_name="communication/communicationpreference_form.html"):
    pref = get_object_or_404(CommunicationPreference, pk=object_id)
    if request.method == "POST":
        form = CommunicationPreferenceForm(data=request.POST, user=request.user, instance=pref)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CommunicationPreferenceForm(user=request.user, instance=pref)
    return render(request, template_name, {
        'form': form
    })
