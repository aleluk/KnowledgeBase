from django.db import models


class Apps(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Apps"

    def __str__(self):
        return f"{self.name}"


class Devices(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Devices"

    def __str__(self):
        return f"{self.name}"


class NetworkInternet(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Network & Internet"

    def __str__(self):
        return f"{self.name}"


class System(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "System"

    def __str__(self):
        return f"{self.name}"


class TCN(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "TCN"

    def __str__(self):
        return f"{self.name}"


class UpdateSecurity(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "UpdateSecurity"

    def __str__(self):
        return f"{self.name}"


# class Index(models.Model):
#     name = models.CharField(max_length=50)
#     update_security_var = models.ForeignKey(UpdateSecurity, on_delete=models.CASCADE, null=True)
#     apps_var = models.ForeignKey(Apps, on_delete=models.CASCADE, null=True)
#     tcn_var = models.ForeignKey(TCN, on_delete=models.CASCADE, null=True)
#     system_var = models.ForeignKey(System, on_delete=models.CASCADE, null=True)
#     network_internet_var = models.ForeignKey(NetworkInternet, on_delete=models.CASCADE, null=True)
#     devices_var = models.ForeignKey(Devices, on_delete=models.CASCADE, null=True)










# class WindowsUpdate(models.Model):
#     # Update & Security node: level 1
#     name = models.CharField(max_length=50)
#     update_security = models.ForeignKey(UpdateSecurity, on_delete=models.CASCADE, null=True)
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class FeatureUpdate(models.Model):
#     # Update & Security node: level 1
#     name = models.CharField(max_length=50)
#     update_security = models.ForeignKey(UpdateSecurity, on_delete=models.CASCADE, null=True)
#
#     def __str__(self):
#         return f"{self.name}"


# class AboutWindowsUpdate(models.Model):
#     # Update & Security node: level 2
#     name = models.CharField(max_length=50)
#     windows_update = models.ForeignKey(WindowsUpdate, on_delete=models.CASCADE, null=True)
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class WindowsUpdateError(models.Model):
#     # Update & Security node: level 2
#     name = models.CharField(max_length=50)
#     windows_update = models.ForeignKey(WindowsUpdate, on_delete=models.CASCADE, null=True)
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class AboutFeatureUpdate(models.Model):
#     # Update & Security node: level 2
#     name = models.CharField(max_length=50)
#     feature_update = models.ForeignKey(FeatureUpdate, on_delete=models.CASCADE, null=True)
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class FeatureUpdateError(models.Model):
#     # Update & Security node: level 2
#     name = models.CharField(max_length=50)
#     feature_update = models.ForeignKey(FeatureUpdate, on_delete=models.CASCADE, null=True)
#
#     def __str__(self):
#         return f"{self.name}"

