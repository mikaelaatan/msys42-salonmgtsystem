# Generated by Django 3.2 on 2021-05-28 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_service_is_working'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='is_working',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
    ]