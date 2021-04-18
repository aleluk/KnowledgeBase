from django.contrib.postgres.search import SearchVectorField
from django.db import models


class UpdateSecurity(models.Model):
    name = models.CharField(max_length=250, null=True)
    antivirus_about = models.TextField()
    antivirus_issues = models.TextField()
    bitlocker_about = models.TextField()
    bitlocker_yes = models.TextField()
    bitlocker_no = models.TextField()
    fu_about = models.TextField()
    fu_errors = models.TextField()
    wu_about = models.TextField()
    wu_errors = models.TextField()
    vector = SearchVectorField(null=True)

    class Meta:
        verbose_name_plural = "UpdateSecurity"

    def __str__(self):
        return f"{self.name}"


class Devices(models.Model):
    name = models.CharField(max_length=250, null=True)
    camera_yes = models.TextField()
    camera_no = models.TextField()
    printers = models.TextField()
    sound_yes = models.TextField()
    sound_no = models.TextField()
    vector = SearchVectorField(null=True)

    class Meta:
        verbose_name_plural = "Devices"

    def __str__(self):
        return f"{self.name}"


# class Apps(models.Model):
#     name = models.CharField(max_length=50)
#
#     class Meta:
#         verbose_name_plural = "Apps"
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class Devices(models.Model):
#     name = models.CharField(max_length=50)
#
#     class Meta:
#         verbose_name_plural = "Devices"
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class Office365(models.Model):
#     name = models.CharField(max_length=50)
#
#     class Meta:
#         verbose_name_plural = "Office365"
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class NetworkInternet(models.Model):
#     name = models.CharField(max_length=50)
#
#     class Meta:
#         verbose_name_plural = "Network & Internet"
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class System(models.Model):
#     name = models.CharField(max_length=50)
#
#     class Meta:
#         verbose_name_plural = "System"
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class TCN(models.Model):
#     name = models.CharField(max_length=50)
#
#     class Meta:
#         verbose_name_plural = "TCN"
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class UpdateSecurity(models.Model):
#     name = models.CharField(max_length=50)
#
#     class Meta:
#         verbose_name_plural = "UpdateSecurity"
#
#     def __str__(self):
#         return f"{self.name}"



