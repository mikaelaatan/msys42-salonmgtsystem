# Generated by Django 3.2 on 2021-04-21 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customerid', models.AutoField(db_column='CustomerID', primary_key=True, serialize=False)),
                ('username', models.CharField(db_column='Username', max_length=15, null=True)),
                ('dateofbirth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staffid', models.AutoField(db_column='StaffID', primary_key=True, serialize=False)),
                ('username', models.CharField(db_column='Username', max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.AutoField(db_column='UserID', primary_key=True, serialize=False)),
                ('firstname', models.CharField(db_column='FirstName', max_length=24)),
                ('lastname', models.CharField(db_column='LastName', max_length=12)),
                ('emailaddress', models.CharField(db_column='EmailAddress', max_length=50)),
                ('contactnumber', models.IntegerField(db_column='ContactNumber')),
                ('username', models.CharField(db_column='Username', max_length=15)),
                ('password', models.CharField(db_column='Password', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceRendered',
            fields=[
                ('servicerenderedid', models.AutoField(db_column='ServiceRenderedID', primary_key=True, serialize=False)),
                ('rating', models.DecimalField(blank=True, db_column='Rating', decimal_places=2, max_digits=2, null=True)),
                ('comment', models.TextField(blank=True, db_column='Comment', null=True)),
                ('totalamount', models.DecimalField(blank=True, db_column='TotalAmount', decimal_places=2, max_digits=10, null=True)),
                ('paymentmethod', models.CharField(db_column='PaymentMethod', max_length=64)),
                ('serviceid', models.ForeignKey(db_column='ServiceID', on_delete=django.db.models.deletion.CASCADE, to='services.service')),
                ('staffid', models.ForeignKey(db_column='StaffID', on_delete=django.db.models.deletion.CASCADE, to='scheduling.staff')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('appointmentid', models.AutoField(db_column='AppointmentID', primary_key=True, serialize=False)),
                ('appointmentdate', models.DateField()),
                ('appointmenttime', models.TimeField()),
                ('iscancelled', models.BooleanField(default='No')),
                ('customerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduling.customer')),
            ],
        ),
    ]
