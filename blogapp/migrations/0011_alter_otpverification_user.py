# Generated by Django 5.1.2 on 2024-10-29 11:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0010_alter_userdata_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpverification',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blogapp.userdata'),
        ),
    ]