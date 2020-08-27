# Generated by Django 3.1 on 2020-08-24 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("retail_app", "0003_auto_20200821_1841"),
    ]

    operations = [
        migrations.CreateModel(
            name="Business_Designer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
            options={"verbose_name_plural": "Business Designers",},
        ),
        migrations.CreateModel(
            name="Product_Color",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("color", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Product_Quantity",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField()),
            ],
        ),
        migrations.RemoveField(model_name="category", name="product",),
        migrations.RemoveField(model_name="designer", name="category",),
        migrations.RemoveField(model_name="designer", name="collection",),
        migrations.RemoveField(model_name="designer", name="product",),
        migrations.RemoveField(model_name="designer", name="season",),
        migrations.RemoveField(model_name="product_stock", name="color",),
        migrations.RemoveField(model_name="product_stock", name="quantity",),
        migrations.AddField(
            model_name="product_description",
            name="brand",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product_stock",
            name="colors",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="retail_app.product_color",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product_stock",
            name="quantities",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="retail_app.product_quantity",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="business",
            name="designer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="retail_app.business_designer",
            ),
        ),
    ]
