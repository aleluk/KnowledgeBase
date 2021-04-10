from django.urls import path, include
from . import views

from .views import IndexView, about_one
from .views import AppsView, DevicesView, NetworkInternetView, SystemView, TcnView, UpdateSecurityView
from .views import NetworkDrive, Performance, RDP, Search
from .views import Trackwise, Apollo, DocuSign, LotusNotes, Adobe, SAP, WaveWare
from .views import WindowsUpdate, FeatureUpdate, Antivirus, Bitlocker
from .views import Internet, VPN, BION

urlpatterns = [
    path('testing/', views.testing, name='testing'),
    path('', IndexView.as_view(), name="index"),
    # path('search/', SearchResultsView.as_view(), name='search_results'),

    path('apps/', AppsView.as_view(), name="apps"),
    path('trackwise/', Trackwise.as_view(), name="trackwise"),
    path('apollo/', Apollo.as_view(), name="apollo"),
    path('docusign/', DocuSign.as_view(), name="docusign"),
    path('lotusnotes/', LotusNotes.as_view(), name="lotus_notes"),
    path('adobe/', Adobe.as_view(), name="adobe"),
    path('sap/', SAP.as_view(), name="sap"),
    path('waveware/', WaveWare.as_view(), name="waveware"),

    path('devices/', DevicesView.as_view(), name="devices"),

    path('network&internet/', NetworkInternetView.as_view(), name="network&internet"),
    path('internet/', Internet.as_view(), name="internet"),
    path('bion/', BION.as_view(), name="bion"),
    path('vpn/', VPN.as_view(), name="vpn"),

    path('system/', SystemView.as_view(), name="system"),
    path('performance/', Performance.as_view(), name="performance"),
    path('network_drive/', NetworkDrive.as_view(), name="network_drive"),
    path('rdp/', RDP.as_view(), name="rdp"),
    path('search_issues/', Search.as_view(), name="search"),

    path('tcn/', TcnView.as_view(), name="tcn"),

    path('update_security/', UpdateSecurityView.as_view(), name='update&security'),
    path('windowsupdate/', WindowsUpdate.as_view(), name='windows_update'),
    path('featureupdate/', FeatureUpdate.as_view(), name='feature_update'),
    path('antivirus/', Antivirus.as_view(), name='antivirus'),
    path('bitlocker/', Bitlocker.as_view(), name='bitlocker'),
    path('about_one/', about_one, name='about_one'),
]
