# Generated by Django 3.2 on 2023-10-06 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0006_alter_person_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='university',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
