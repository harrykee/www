# Generated by Django 2.0 on 2018-04-28 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_importfile_knsvnhistory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrollline',
            name='school',
        ),
        migrations.DeleteModel(
            name='ImportFile',
        ),
        migrations.DeleteModel(
            name='KNSVNHistory',
        ),
        migrations.DeleteModel(
            name='EnrollLine',
        ),
    ]
