# Generated by Django 2.2.13 on 2020-06-19 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('research_reports', '0004_report_fields_not_required'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportsection',
            name='html_id',
        ),
        migrations.RemoveField(
            model_name='reportsubsection',
            name='sub_id',
        ),
    ]