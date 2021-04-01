from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView
# from .models import UpdateSecurity, WindowsUpdate, FeatureUpdate
from django.views.generic.base import TemplateView, View


def testing(request):
    return HttpResponse('Testing in progress')


def index(request):
    return render(
        request,
        template_name="index.html"
    )

# All Apps:
class Apps(TemplateView):
    template_name = "apps.html"


class Trackwise(TemplateView):
    template_name = "trackwise.html"


class Apollo(TemplateView):
    template_name = "apollo.html"


class DocuSign(TemplateView):
    template_name = "docusign.html"


class LotusNotes(TemplateView):
    template_name = "lotus_notes.html"


class Adobe(TemplateView):
    template_name = "adobe.html"


class SAP(TemplateView):
    template_name = "sap.html"


class WaveWare(TemplateView):
    template_name = "waveware.html"

# All Devices
class Devices(TemplateView):
    template_name = "devices.html"


#All Network & Internet:
class Internet(TemplateView):
    template_name = "network&internet.html"


#All System:
class System(TemplateView):
    template_name = "system.html"


#All TCN:
class Tcn(TemplateView):
    template_name = "tcn.html"


#All Update & Security:
class UpdateSecurity(TemplateView):
    template_name = "update_security.html"


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # wu = Windows Update
    #     # fu = Feature Update
    #     context["wu"] = UpdateSecurity.objects.get(id=1)
    #     context["fu"] = UpdateSecurity.objects.get(id=2)
    #     return context


class WindowsUpdate(TemplateView):
    template_name = "windows_update.html"


class FeatureUpdate(TemplateView):
    template_name = "feature_update.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["about_2"] = FeatureUpdate.objects.get(id=1)
    #     context["errors_2"] = FeatureUpdate.objects.get(id=2)
    #     return context


class Antivirus(TemplateView):
    template_name = "antivirus.html"


class Bitlocker(TemplateView):
    template_name = "bitlocker.html"


def about_one(request):
    return HttpResponseRedirect("about_one")
