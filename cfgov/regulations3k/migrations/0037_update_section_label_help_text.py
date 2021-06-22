# Generated by Django 2.2.20 on 2021-04-22 14:31

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('regulations3k', '0036_update_notification_default_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subpart',
            name='label',
            field=models.CharField(help_text='Labels must be unique within this regulation version and always require at least 1 alphanumeric character, then any number of alphanumeric characters and hyphens, with no spaces.', max_length=255, validators=[django.core.validators.RegexValidator(re.compile('^[\\w]+[-\\w]*$'), 'Enter a valid “label” consisting of letters, numbers, hyphens, and no spaces.', 'invalid')]),
        ),
    ]