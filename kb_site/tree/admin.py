from django.contrib import admin
from .models import (
    UpdateSecurity,
    WindowsUpdate,
    FeatureUpdate,
    # WindowsUpdateError,
    # FeatureUpdateError,
    # AboutWindowsUpdate,
    # AboutFeatureUpdate,
)

# Register your models here.
admin.site.register(UpdateSecurity)
admin.site.register(WindowsUpdate)
admin.site.register(FeatureUpdate)
# admin.site.register(WindowsUpdateError)
# admin.site.register(FeatureUpdateError)
# admin.site.register(AboutWindowsUpdate)
# admin.site.register(AboutFeatureUpdate)