from django.contrib import admin
from .models import (
    Apps,
    Devices,
    NetworkInternet,
    System,
    TCN,
    UpdateSecurity,
)

# Register your models here.
admin.site.register(Apps)
admin.site.register(Devices)
admin.site.register(NetworkInternet)
admin.site.register(System)
admin.site.register(TCN)
admin.site.register(UpdateSecurity)

