# Generated by Django 3.1 on 2020-08-25 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("retail_app", "0005_product_designer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product_quantity",
            name="quantity",
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
