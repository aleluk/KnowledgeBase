from django.urls import path
from . import views
from .views import index, about_one
from .views import Apps, Devices, Internet, System, Tcn, UpdateSecurity
from. views import Trackwise, Apollo, DocuSign, LotusNotes, Adobe, SAP, WaveWare
from. views import WindowsUpdate, FeatureUpdate, Antivirus, Bitlocker

urlpatterns = [
    path('testing/', views.testing, name='testing'),
    path('', index, name="index"),

    path('apps/', Apps.as_view(), name="apps"),
    path('trackwise/', Trackwise.as_view(), name="trackwise"),
    path('apollo/', Apollo.as_view(), name="apollo"),
    path('docusign/', DocuSign.as_view(), name="docusign"),
    path('lotusnotes/', LotusNotes.as_view(), name="lotus_notes"),
    path('adobe/', Adobe.as_view(), name="adobe"),
    path('sap/', SAP.as_view(), name="sap"),
    path('waveware/', WaveWare.as_view(), name="waveware"),

    path('devices/', Devices.as_view(), name="devices"),
    path('internet/', Internet.as_view(), name="internet"),
    path('system/', System.as_view(), name="system"),
    path('tcn/', Tcn.as_view(), name="tcn"),
    path('update_security/', UpdateSecurity.as_view(), name='update&security'),
    path('windowsupdate/', WindowsUpdate.as_view(), name='windows_update'),
    path('featureupdate/', FeatureUpdate.as_view(), name='feature_update'),
    path('antivirus/', Antivirus.as_view(), name='antivirus'),
    path('bitlocker/', Bitlocker.as_view(), name='bitlocker'),
    path('about_one/', about_one, name='about_one'),
]