# Generated by Django 2.1.3 on 2018-11-05 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magzapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='referencefrequency',
            name='ref_desciption',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
