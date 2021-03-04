# Generated by Django 3.0.3 on 2021-03-02 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceRendered',
            fields=[
                ('servicerenderedid', models.AutoField(db_column='ServiceRenderedID', primary_key=True, serialize=False)),
                ('rating', models.DecimalField(blank=True, db_column='Rating', decimal_places=2, max_digits=2, null=True)),
                ('comment', models.TextField(blank=True, db_column='Comment', null=True)),
                ('totalamount', models.DecimalField(blank=True, db_column='TotalAmount', decimal_places=2, max_digits=10, null=True)),
                ('paymentmethod', models.CharField(db_column='PaymentMethod', max_length=64)),
                ('serviceid', models.ForeignKey(db_column='ServiceID', on_delete=django.db.models.deletion.CASCADE, to='scheduling.Service')),
                ('staffid', models.ForeignKey(db_column='StaffID', on_delete=django.db.models.deletion.CASCADE, to='scheduling.Staff')),
            ],
        ),
    ]