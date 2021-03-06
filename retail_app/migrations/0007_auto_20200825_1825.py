# Generated by Django 3.1 on 2020-08-25 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("retail_app", "0006_auto_20200825_1337"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Business_Designer",
            new_name="BusinessDesigner",
        ),
        migrations.RenameModel(
            old_name="Product_Color",
            new_name="ProductColor",
        ),
        migrations.RenameModel(
            old_name="Product_Description",
            new_name="ProductDescription",
        ),
        migrations.RenameModel(
            old_name="Product_Details",
            new_name="ProductDetails",
        ),
        migrations.RenameModel(
            old_name="Product_Image",
            new_name="ProductImage",
        ),
        migrations.RenameModel(
            old_name="Product_Price",
            new_name="ProductPrice",
        ),
        migrations.RenameModel(
            old_name="Product_Quantity",
            new_name="ProductQuantity",
        ),
        migrations.RenameModel(
            old_name="Product_Stock",
            new_name="ProductStock",
        ),
        migrations.AlterModelOptions(
            name="productprice",
            options={"verbose_name_plural": "Product Prices"},
        ),
    ]
