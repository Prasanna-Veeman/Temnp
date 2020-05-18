# Generated by Django 3.0.3 on 2020-05-18 07:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_auto_20200515_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='ctime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='uptime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]