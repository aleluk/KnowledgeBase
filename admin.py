from django.contrib import admin
from .models import (
    UpdateSecurity,
    WindowsUpdate,
    FeatureUpdate,
    Error1,
    Error2,
    AboutWindowsUpdate,
    About2,
)

# Register your models here.
admin.site.register(UpdateSecurity)
admin.site.register(WindowsUpdate)
admin.site.register(FeatureUpdate)
admin.site.register(Error1)
admin.site.register(Error2)
admin.site.register(AboutWindowsUpdate)
admin.site.register(About2)