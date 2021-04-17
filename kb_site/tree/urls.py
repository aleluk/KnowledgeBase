from django.urls import path, include
from . import views
from .views import search, AppsView, DevicesView, NetworkInternetView, Office365View, SystemView, \
    UpdateSecurityView
from .views import (
    AntivirusAbout,
    AntivirusIssues,
    BitlockerAbout,
    BitlockerYes,
    BitlockerNo,
    FeatureUpdateAbout,
    FeatureUpdateErrors,
    WindowsUpdateErrors,
    WindowsUpdateAbout,
)

app_name = 'tree'
urlpatterns = [
    # path('/index', IndexView.as_view(), name="index"),
    path('', search, name='search'),

    path('antivirus_about/', AntivirusAbout.as_view(), name="antivirus_about"),
    path('antivirus_issues/', AntivirusIssues.as_view(), name="antivirus_issues"),
    path('bitlocker_about/', BitlockerAbout.as_view(), name="bitlocker_about"),
    path('bitlocker_yes/', BitlockerYes.as_view(), name="bitlocker_yes"),
    path('bitlocker_no/', BitlockerNo.as_view(), name="bitlocker_no"),
    path('featureupdate_about/', FeatureUpdateAbout.as_view(), name="fu_about"),
    path('featureupdate_errors/', FeatureUpdateErrors.as_view(), name='fu_errors'),
    path('windowsupdate_about/', WindowsUpdateAbout.as_view(), name='wu_about'),
    path('windowsupdate_errors/', WindowsUpdateErrors.as_view(), name='wu_errors'),

    path('apps/', AppsView.as_view(), name="apps"),
    path('devices/', DevicesView.as_view(), name="devices"),
    path('network&internet/', NetworkInternetView.as_view(), name="network&internet"),
    path('office365/', Office365View.as_view(), name="office365"),
    path('system/', SystemView.as_view(), name="system"),
    path('update_security/', UpdateSecurityView.as_view(), name='update&security'),
]
