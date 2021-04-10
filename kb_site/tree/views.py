from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic import FormView, ListView, TemplateView, View
from .forms import SearchForm
from .models import UpdateSecurity


class IndexView(ListView):
    model = UpdateSecurity
    template_name = "index.html"

    # def get_queryset(self):
    #     query = self.request.GET.get('q', '')
    #     object_list = UpdateSecurity.objects.filter(name__icontains=query)
    #     return object_list


class HomePageView(FormView):
    template_name = "index.html"
    form_class = SearchForm


# All Apps:
class AppsView(TemplateView):
    template_name = "apps.html"


class Trackwise(TemplateView):
    template_name = "apps.html"


class Apollo(TemplateView):
    template_name = "apps.html"


class DocuSign(TemplateView):
    template_name = "apps.html"


class LotusNotes(TemplateView):
    template_name = "apps.html"


class Adobe(TemplateView):
    template_name = "apps.html"


class SAP(TemplateView):
    template_name = "apps.html"


class WaveWare(TemplateView):
    template_name = "apps.html"

# All Devices
class DevicesView(TemplateView):
    template_name = "devices.html"


#All Network & Internet:
class NetworkInternetView(TemplateView):
    template_name = "network&internet.html"


class Internet(TemplateView):
    template_name = "network&internet.html"


class VPN(TemplateView):
    template_name = "network&internet.html"


class BION(TemplateView):
    template_name = "network&internet.html"


#All System:
class SystemView(TemplateView):
    template_name = "system.html"


class Performance(TemplateView):
    template_name = "system.html"


class NetworkDrive(TemplateView):
    template_name = "system.html"


class RDP(TemplateView):
    template_name = "system.html"


class Search(TemplateView):
    template_name = "system.html"


#All TCN:
class TcnView(TemplateView):
    template_name = "tcn.html"


#All Update & Security:
class UpdateSecurityView(TemplateView):
    template_name = "update_security.html"


class WindowsUpdate(TemplateView):
    template_name = "update_security.html"


class FeatureUpdate(TemplateView):
    template_name = "update_security.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about_2"] = WindowsUpdate.objects.get(id=1)
        context["errors_2"] = WindowsUpdate.objects.get(id=2)
        return context


class Antivirus(TemplateView):
    template_name = "update_security.html"


class Bitlocker(TemplateView):
    template_name = "update_security.html"

