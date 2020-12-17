# Generated by Django 3.1.3 on 2020-12-01 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='resumeTemplatesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameOfResume', models.CharField(max_length=1000)),
                ('doc', models.FileField(upload_to='doc/')),
                ('image', models.FileField(upload_to='image/')),
            ],
        ),
    ]