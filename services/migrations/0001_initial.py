# Generated by Django 3.0.3 on 2021-03-05 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ServiceName', models.CharField(max_length=64)),
                ('ServiceType', models.CharField(max_length=32)),
                ('ServicePrice', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('ServiceDescription', models.TextField(blank=True, null=True)),
                ('ServiceDuration', models.CharField(max_length=32)),
            ],
        ),
    ]