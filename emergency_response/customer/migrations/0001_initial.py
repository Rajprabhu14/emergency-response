# Generated by Django 3.0.4 on 2020-03-29 07:16

import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=500)),
                ('grocery', django.contrib.postgres.fields.jsonb.JSONField()),
                ('landmark', models.CharField(max_length=255)),
                ('order_status', models.CharField(choices=[('N', 'Not Verified'), ('V', 'Verified'), ('T', 'Taken'), ('I', 'InTransit'), ('D', 'Deliveried'), ('U', 'unreachable')], default='N', max_length=2)),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('verfication_completed', models.BooleanField(default=False)),
                ('other_detail', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'customer_details',
                'ordering': ['-verfication_completed'],
            },
        ),
    ]
