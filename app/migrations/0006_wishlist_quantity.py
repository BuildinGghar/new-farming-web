# Generated by Django 4.2.3 on 2023-07-22 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_orderplaced_status_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
