# Generated by Django 3.2 on 2021-04-29 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('staff', '0002_remove_staffmodel_average_rating'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avg_rating', models.DecimalField(blank=True, db_column='Rating', decimal_places=1, max_digits=2, null=True)),
                ('comment', models.TextField(blank=True, db_column='Comment', null=True)),
                ('appointmentdate', models.DateField(blank=True, db_column='Appointment Date', null=True)),
                ('appointmenttime', models.CharField(blank=True, db_column='Appointment Time', max_length=10, null=True)),
                ('iscancelled', models.BooleanField(db_column='Cancelled', default='No')),
                ('customers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
                ('services', models.ForeignKey(db_column='ServiceID', on_delete=django.db.models.deletion.CASCADE, to='services.service')),
                ('staffs', models.ForeignKey(db_column='StaffID', on_delete=django.db.models.deletion.CASCADE, to='staff.staffmodel')),
            ],
        ),
    ]
