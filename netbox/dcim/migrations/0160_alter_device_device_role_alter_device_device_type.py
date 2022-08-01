# Generated by Django 4.0.6 on 2022-08-01 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0159_alter_device_ip_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='device_role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='devices', to='dcim.devicerole'),
        ),
        migrations.AlterField(
            model_name='device',
            name='device_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='instances', to='dcim.devicetype'),
        ),
    ]
