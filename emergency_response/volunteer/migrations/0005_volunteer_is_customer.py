# Generated by Django 3.0.4 on 2020-04-10 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0004_auto_20200329_0747'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='is_customer',
            field=models.BooleanField(default=False),
        ),
    ]