from django.urls import path, include
from . import views
from .views import IndexView, HomePageView
from .views import AppsView, DevicesView, NetworkInternetView, SystemView, TcnView, UpdateSecurityView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('search/', HomePageView.as_view(), name='search_results'),

    path('apps/', AppsView.as_view(), name="apps"),
    path('devices/', DevicesView.as_view(), name="devices"),
    path('network&internet/', NetworkInternetView.as_view(), name="network&internet"),
    path('system/', SystemView.as_view(), name="system"),
    path('tcn/', TcnView.as_view(), name="tcn"),
    path('update_security/', UpdateSecurityView.as_view(), name='update&security'),
]
