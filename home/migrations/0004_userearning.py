# Generated by Django 3.2.5 on 2021-10-03 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_user_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserEarning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.CharField(max_length=40)),
                ('earning', models.IntegerField()),
                ('livevids', models.IntegerField()),
            ],
        ),
    ]