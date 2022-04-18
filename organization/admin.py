from django.contrib import admin
from organization import models

# Register your models here.

admin.site.register(models.Entity)
admin.site.register(models.Location)
admin.site.register(models.Department)
admin.site.register(models.Vendor)
admin.site.register(models.Requests)