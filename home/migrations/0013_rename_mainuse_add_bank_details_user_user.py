# Generated by Django 3.2.5 on 2021-10-08 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20211009_0347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='add_bank_details_user',
            old_name='mainuse',
            new_name='user',
        ),
    ]