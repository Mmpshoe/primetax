# Generated by Django 3.2.12 on 2023-06-12 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_bankdetails_bankdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_registered',
            field=models.BooleanField(default=False),
        ),
    ]