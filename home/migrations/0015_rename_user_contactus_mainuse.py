# Generated by Django 3.2.5 on 2021-10-08 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_contactus_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='user',
            new_name='mainuse',
        ),
    ]
