# Generated by Django 3.2 on 2024-01-09 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0011_person_activation_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='invitation_expires_at',
        ),
        migrations.RemoveField(
            model_name='person',
            name='invitation_token',
        ),
        migrations.RemoveField(
            model_name='person',
            name='is_superuser',
        ),
    ]
