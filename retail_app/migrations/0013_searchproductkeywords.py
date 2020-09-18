# Generated by Django 3.1 on 2020-09-04 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("retail_app", "0012_auto_20200831_1627"),
    ]

    operations = [
        migrations.CreateModel(
            name="SearchProductKeywords",
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
                ("keywords", models.TextField()),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="retail_app.product",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Search All Product Keywords",
            },
        ),
    ]
