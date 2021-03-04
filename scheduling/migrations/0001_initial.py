# Generated by Django 3.0.3 on 2021-03-02 07:56

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
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staffid', models.AutoField(db_column='StaffID', primary_key=True, serialize=False)),
                ('firstname', models.CharField(db_column='FirstName', max_length=32)),
                ('lastname', models.CharField(db_column='LastName', max_length=32)),
            ],
        ),
    ]