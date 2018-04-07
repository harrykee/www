# Generated by Django 2.0 on 2018-04-05 08:01

from django.db import migrations, models
import system.storage


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_head',
            field=models.ImageField(storage=system.storage.ImageStorage(), upload_to='./head/', verbose_name='用户头像'),
        ),
    ]
