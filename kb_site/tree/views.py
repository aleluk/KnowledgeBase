from django.http import HttpResponse
from django.shortcuts import render
from .models import UpdateSecurity, WindowsUpdate, FeatureUpdate
from django.views.generic.base import TemplateView


def testing(request):
    return HttpResponse('Testing in progress')


class UpdateSecurityTemplateView(TemplateView):
    template_name = "update_security.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # wu = Windows Update
        # fu = Feature Update
        context["wu"] = UpdateSecurity.objects.get(id=1)
        context["fu"] = UpdateSecurity.objects.get(id=2)
        return context


class WindowsUpdateTemplateView(TemplateView):
    template_name = "windows_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about_1"] = WindowsUpdate.objects.get(id=1)
        context["errors_1"] = WindowsUpdate.objects.get(id=2)
        return context


class FeatureUpdateTemplateView(TemplateView):
    template_name = "feature_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about_2"] = FeatureUpdate.objects.get(id=1)
        context["errors_2"] = FeatureUpdate.objects.get(id=2)
        return context
