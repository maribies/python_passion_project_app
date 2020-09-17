# Generated by Django 3.1 on 2020-08-31 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("retail_app", "0008_auto_20200826_2328"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="productcolor",
            options={"verbose_name_plural": "Product Stock"},
        ),
        migrations.RenameField(
            model_name="productstock",
            old_name="colors",
            new_name="color_stock",
        ),
        migrations.RemoveField(
            model_name="product",
            name="image",
        ),
        migrations.RemoveField(
            model_name="product",
            name="stock",
        ),
        migrations.RemoveField(
            model_name="productimage",
            name="image",
        ),
        migrations.RemoveField(
            model_name="productimage",
            name="name",
        ),
        migrations.RemoveField(
            model_name="productstock",
            name="name",
        ),
        migrations.RemoveField(
            model_name="productstock",
            name="quantities",
        ),
        migrations.AddField(
            model_name="productimage",
            name="image_url",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="productimage",
            name="product",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="retail_app.product",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="productquantity",
            name="colors",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="retail_app.productcolor",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="productstock",
            name="product",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="retail_app.product",
            ),
            preserve_default=False,
        ),
    ]
