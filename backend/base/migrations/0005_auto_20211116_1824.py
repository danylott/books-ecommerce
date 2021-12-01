# Generated by Django 3.2.8 on 2021-11-16 18:24

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("base", "0004_realestate_image"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="RealEstate",
            new_name="Product",
        ),
        migrations.RenameField(
            model_name="orderitem",
            old_name="realEstate",
            new_name="product",
        ),
        migrations.RenameField(
            model_name="review",
            old_name="realEstate",
            new_name="product",
        ),
    ]
