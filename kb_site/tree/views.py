from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView
# from .models import UpdateSecurity, WindowsUpdate, FeatureUpdate
from django.views.generic import FormView, ListView, TemplateView, View

from .models import UpdateSecurity


def testing(request):
    return HttpResponse('Testing in progress')


class IndexView(ListView):
    model = UpdateSecurity
    template_name = "index.html"

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        object_list = UpdateSecurity.objects.filter(name__icontains=query)
        return object_list


        # form_class = SearchForm
    # class SearchResultsView(ListView):
    #     model = UpdateSecurity
    #     template_name = 'index.html'


# All Apps:
class AppsView(TemplateView):
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
class DevicesView(TemplateView):
    template_name = "devices.html"


#All Network & Internet:
class NetworkInternetView(TemplateView):
    template_name = "network&internet.html"


class Internet(TemplateView):
    template_name = "internet.html"


class VPN(TemplateView):
    template_name = "VPN.html"


class BION(TemplateView):
    template_name = "bion.html"


#All System:
class SystemView(TemplateView):
    template_name = "system.html"


class Performance(TemplateView):
    template_name = "performance.html"


class NetworkDrive(TemplateView):
    template_name = "network_drive.html"


class RDP(TemplateView):
    template_name = "rdp.html"


class Search(TemplateView):
    template_name = "search.html"


#All TCN:
class TcnView(TemplateView):
    template_name = "tcn.html"


#All Update & Security:
class UpdateSecurityView(TemplateView):
    template_name = "update_security.html"


class WindowsUpdate(TemplateView):
    template_name = "windows_update.html"


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # wu = Windows Update
    #     # fu = Feature Update
    #     context["wu"] = UpdateSecurity.objects.get(id=1)
    #     context["fu"] = UpdateSecurity.objects.get(id=2)
    #     return context


class FeatureUpdate(DetailView):
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
    return render(
        request,
        template_name="about_one.html"
    )
