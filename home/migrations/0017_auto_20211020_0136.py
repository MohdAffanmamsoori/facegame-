# Generated by Django 3.2.5 on 2021-10-19 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_contactus_mainuse'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_bank_details_user',
            name='profile_name',
            field=models.CharField(default=1, max_length=100),
        ),
        migrations.AddField(
            model_name='add_bank_details_user',
            name='profile_url',
            field=models.CharField(default=1, max_length=500),
        ),
    ]
