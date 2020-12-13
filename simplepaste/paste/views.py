from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from .models import PasteBox
from .forms import PasteForm


def index(request):
    latest_pastes = PasteBox.objects.order_by('-id')[:5]
    form = PasteForm()
    if request.method == "POST":
        try:
            last_id = PasteBox.objects.order_by('-id')[0].id
            form = PasteForm(request.POST)
            form.save()
            return HttpResponseRedirect("/paste/" + str(last_id + 1) + "/")
        except ValueError:
            pass
    return render(request, "paste/index.html", {"latest_pastes": latest_pastes, "form": form})


def paste(request, paste_id):
    try:
        paste = PasteBox.objects.get(pk=paste_id)
    except PasteBox.DoesNotExist:
        raise Http404("Paste does not exist")
    return render(request, 'paste/paste.html', {'paste': paste})
