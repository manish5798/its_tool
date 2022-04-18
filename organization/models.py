from django.contrib.auth import get_user_model
from django.db import models
from its_tool.users.models import Address

def logos_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / logos / Entity_<id>/<filename>
    return "logos/{}.{}".format(filename, "jpg")

class Entity(models.Model):
    
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.CharField(max_length=255, blank=False, null=False)
    contact_no = models.CharField(max_length=255, blank=False, null=False)
    email = models.CharField(unique=True, max_length=255, blank=False, null=False)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    logo = models.FileField(upload_to=logos_directory_path, max_length=254, blank=True, null=True)
    users = models.ManyToManyField(get_user_model(), blank=True)


class Location(models.Model):
    name = models.CharField("Location Name", max_length=255, blank=False, null=False)
    latitude = models.CharField("Location Latitude", max_length=255, blank=False, null=False)
    longitude = models.CharField("Location Longitude", max_length=255, blank=False, null=False)
    pincode = models.CharField("Location Pincode", max_length=255, blank=True, null=True)
    description = models.CharField("Location Description", max_length=255, blank=True, null=True)


class Department(models.Model):
    name = models.CharField("Department Name", max_length=255, blank=True, null=True)
    users = models.ManyToManyField(get_user_model(), blank=True)


class Vendor(models.Model):
    name = models.CharField("Vendor Name", max_length=255, blank=True, null=True)
    code = models.CharField("Vendor Code", max_length=255, blank=True, null=True)
    users = models.ManyToManyField(get_user_model(), blank=True)


class Requests(models.Model):
    consignor = models.ForeignKey(get_user_model(), blank=False, null=False, on_delete=models.PROTECT)
    shipment_pickup = models.CharField("Vendor Code", max_length=255, blank=True, null=True)
    shipment_location = models.ForeignKey(Location, related_name="requests", on_delete=models.CASCADE)
    employee_name = models.CharField("Employee Name", max_length=255, blank=True, null=True)
    employee_service_line = models.CharField("Employee Service Line", max_length=255, blank=True, null=True)
    serial_number = models.CharField("Serial Number", max_length=255, blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    assets = models.CharField("Assets", max_length=255, blank=True, null=True)
    assets_description = models.CharField("Assets Description", max_length=255, blank=True, null=True)
    laptop_taxable_value = models.CharField("Taxable Value", max_length=255, blank=True, null=True)
    transporter = models.CharField("Transporter", max_length=255, blank=True, null=True)
    transporter_gstin = models.CharField("GSTIN Transporter", max_length=255, blank=True, null=True)
    email = models.CharField("Mail ID", max_length=255, blank=True, null=True)
    phone = models.CharField("Phone Number", max_length=255, blank=True, null=True)
    status = models.CharField("Vendor Delivery Status", max_length=255, blank=True, null=True)
    confirmation_status = models.CharField("Employee Delivery Status", max_length=255, blank=True, null=True)