# Generated by Django 4.2.7 on 2023-11-25 08:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("asset", "0008_remove_asset_condition_delete_assetcondition"),
    ]

    operations = [
        migrations.AddField(
            model_name="asset",
            name="byod",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="asset",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images"),
        ),
        migrations.AddField(
            model_name="asset",
            name="imei",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="asset",
            name="supplier",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="asset",
            name="warranty",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
