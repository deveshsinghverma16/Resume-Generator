# Generated by Django 3.1.3 on 2020-12-03 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_auto_20201202_2214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='additionaldetailsmodel',
            name='selfDescription',
        ),
    ]
