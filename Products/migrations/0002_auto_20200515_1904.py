# Generated by Django 3.0.3 on 2020-05-15 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('location', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='images/'),
        ),
    ]