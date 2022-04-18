from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
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


class Department(models.Model):
    name = models.CharField("Department Name", max_length=255, blank=True, null=True)
    users = models.ManyToManyField(get_user_model(), blank=True)


class Vendor(models.Model):
    name = models.CharField("Vendor Name", max_length=255, blank=True, null=True)
    code = models.CharField("Vendor Code", max_length=255, blank=True, null=True)
    users = models.ManyToManyField(get_user_model(), blank=True)


def eway_bill_directory_path(instance, filename):

    return "eway_bill/{}.{}".format(filename, "jpg")

def delivery_challan_directory_path(instance, filename):

    return "delivery_challan/{}.{}".format(filename, "jpg")


class Requests(models.Model):
    consignor = models.ForeignKey(get_user_model(), blank=False, null=False, on_delete=models.PROTECT)
    shipment_pickup = models.CharField("Shipment Pickup", max_length=255, blank=True, null=True)
    shipment_location = models.CharField("Shipment Location", max_length=255, blank=True, null=True)
    employee_name = models.CharField("Employee Name", max_length=255, blank=True, null=True)
    employee_service_line = models.CharField("Employee Service Line", max_length=255, blank=True, null=True)
    serial_number = models.CharField("Serial Number", max_length=255, blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    assets = models.CharField("Assets", max_length=255, blank=True, null=True)
    assets_description = models.CharField("Assets Description", max_length=255, blank=True, null=True)
    taxable_value = models.CharField("Taxable Value", max_length=255, blank=True, null=True)
    transporter = models.CharField("Transporter", max_length=255, blank=True, null=True)
    transporter_gstin = models.CharField("GSTIN Transporter", max_length=255, blank=True, null=True)
    email = models.CharField("Mail ID", max_length=255, blank=True, null=True)
    phone = models.CharField("Phone Number", max_length=255, blank=True, null=True)
    alternate = models.CharField("Alternate", max_length=255, blank=True, null=True)
    eway_bill = models.FileField(upload_to=eway_bill_directory_path, max_length=254, blank=True, null=True)
    delivery_challan = models.FileField(upload_to=delivery_challan_directory_path, max_length=254, blank=True, null=True)
    vendor = models.ForeignKey(Vendor, related_name="requests", blank=True, null=True, on_delete=models.CASCADE)
    status = models.CharField("Vendor Delivery Status", max_length=255, blank=True, null=True)
    confirmation_status = models.CharField("Employee Delivery Status", max_length=255, blank=True, null=True)
    its_approved = models.BooleanField(default=False)
    dc_approved = models.BooleanField(default=False)
    mailroom_approved = models.BooleanField(default=False)


class Activity(models.Model):
    request_id = models.ForeignKey(Requests, related_name="events", on_delete=models.CASCADE)
    activity = models.CharField("Activity", max_length=255, blank=False, null=False)
    location = models.CharField("Activity Location", max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)