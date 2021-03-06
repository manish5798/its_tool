# Generated by Django 3.2.13 on 2022-04-18 07:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import organization.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Location Name')),
                ('latitude', models.CharField(max_length=255, verbose_name='Location Latitude')),
                ('longitude', models.CharField(max_length=255, verbose_name='Location Longitude')),
                ('pincode', models.CharField(blank=True, max_length=255, null=True, verbose_name='Location Pincode')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Location Description')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Vendor Name')),
                ('code', models.CharField(blank=True, max_length=255, null=True, verbose_name='Vendor Code')),
                ('users', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipment_pickup', models.CharField(blank=True, max_length=255, null=True, verbose_name='Vendor Code')),
                ('employee_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Employee Name')),
                ('employee_service_line', models.CharField(blank=True, max_length=255, null=True, verbose_name='Employee Service Line')),
                ('serial_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='Serial Number')),
                ('assets', models.CharField(blank=True, max_length=255, null=True, verbose_name='Assets')),
                ('assets_description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Assets Description')),
                ('laptop_taxable_value', models.CharField(blank=True, max_length=255, null=True, verbose_name='Taxable Value')),
                ('transporter', models.CharField(blank=True, max_length=255, null=True, verbose_name='Transporter')),
                ('transporter_gstin', models.CharField(blank=True, max_length=255, null=True, verbose_name='GSTIN Transporter')),
                ('email', models.CharField(blank=True, max_length=255, null=True, verbose_name='Mail ID')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Phone Number')),
                ('status', models.CharField(blank=True, max_length=255, null=True, verbose_name='Vendor Delivery Status')),
                ('confirmation_status', models.CharField(blank=True, max_length=255, null=True, verbose_name='Employee Delivery Status')),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.address')),
                ('consignor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('shipment_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='organization.location')),
            ],
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('contact_no', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('logo', models.FileField(blank=True, max_length=254, null=True, upload_to=organization.models.logos_directory_path)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.address')),
                ('users', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Department Name')),
                ('users', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
