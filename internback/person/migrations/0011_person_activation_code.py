# Generated by Django 3.2 on 2024-01-09 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0010_remove_person_activation_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='activation_code',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
