# Generated by Django 3.0.4 on 2020-04-03 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_userprofileinfo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfileInfo',
        ),
    ]