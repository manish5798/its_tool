# Generated by Django 3.2.13 on 2022-04-18 07:55

from django.db import migrations, models
import django.db.models.deletion
import organization.models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requests',
            name='alternate',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Alternate'),
        ),
        migrations.AddField(
            model_name='requests',
            name='delivery_challan',
            field=models.FileField(blank=True, max_length=254, null=True, upload_to=organization.models.delivery_challan_directory_path),
        ),
        migrations.AddField(
            model_name='requests',
            name='eway_bill',
            field=models.FileField(blank=True, max_length=254, null=True, upload_to=organization.models.eway_bill_directory_path),
        ),
        migrations.AddField(
            model_name='requests',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='organization.vendor'),
        ),
    ]
