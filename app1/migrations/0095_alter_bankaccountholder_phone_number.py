# Generated by Django 4.2.2 on 2023-08-12 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0094_bankaccountholder_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccountholder',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
