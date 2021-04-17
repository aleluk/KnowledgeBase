from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic import FormView, ListView, TemplateView, View
from .forms import SearchForm


def search(request):
    my_form = SearchForm()
    if request.method == 'GET':
        return render(request, 'index.html', {'form': my_form})


class WindowsUpdateAbout(TemplateView):
    template_name = "windowsupdate_about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about_1"] = UpdateSecurityView.objects.get(id=1)
        return context


class WindowsUpdateErrors(TemplateView):
    template_name = "windowsupdate_errors.html"


class FeatureUpdateAbout(TemplateView):
    template_name = "featureupdate_about.html"


class FeatureUpdateErrors(TemplateView):
    template_name = "featureupdate_errors.html"


class AntivirusAbout(TemplateView):
    template_name = "antivirus_about.html"


class AntivirusIssues(TemplateView):
    template_name = "antivirus_issues.html"


class BitlockerAbout(TemplateView):
    template_name = "bitlocker_about.html"


# Bitlocker locked: is it a new computer or newly installed Windows? If yes:
class BitlockerYes(TemplateView):
    template_name = "bitlocker_yes.html"


# Bitlocker locked: is it a new computer or newly installed Windows? If no:
class BitlockerNo(TemplateView):
    template_name = "bitlocker_no.html"


# Views for the index page
class AppsView(TemplateView):
    template_name = "applications.html"


class DevicesView(TemplateView):
    template_name = "devices.html"


class Office365View(TemplateView):
    template_name = "office365.html"


class NetworkInternetView(TemplateView):
    template_name = "network&internet.html"


class SystemView(TemplateView):
    template_name = "system.html"


class UpdateSecurityView(TemplateView):
    template_name = "update_security.html"


# class IndexView(ListView):
#     model = UpdateSecurity
#     template_name = "index.html"

    # def get_queryset(self):
    #     query = self.request.GET.get('q', '')
    #     object_list = UpdateSecurity.objects.filter(name__icontains=query)
    #     return object_list


# class HomePageView(FormView):
#     template_name = "index.html"
#     form_class = SearchForm


