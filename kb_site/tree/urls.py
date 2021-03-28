from django.urls import path
from . import views
from .views import UpdateSecurityTemplateView, WindowsUpdateTemplateView, FeatureUpdateTemplateView

urlpatterns = [
    path('testing/', views.testing, name='testing'),
    path('update&security/', UpdateSecurityTemplateView.as_view()),
    path('windowsupdate/', WindowsUpdateTemplateView.as_view()),
    path('featureupdate/', FeatureUpdateTemplateView.as_view()),
]