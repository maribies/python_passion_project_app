# Generated by Django 3.1.1 on 2020-10-01 18:10

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ("retail_app", "0016_auto_20200928_1745"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="product",
            managers=[
                ("products_fully_loaded", django.db.models.manager.Manager()),
            ],
        ),
        migrations.DeleteModel(
            name="Business",
        ),
        migrations.DeleteModel(
            name="BusinessDesigner",
        ),
        migrations.DeleteModel(
            name="Category",
        ),
    ]
