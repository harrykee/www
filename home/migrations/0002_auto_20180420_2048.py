# Generated by Django 2.0 on 2018-04-20 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questions',
            options={'verbose_name': '用户提的问题', 'verbose_name_plural': '用户提的问题'},
        ),
        migrations.AlterField(
            model_name='news',
            name='new_date',
            field=models.DateTimeField(verbose_name='消息时间'),
        ),
        migrations.AlterField(
            model_name='queanswer',
            name='ans_time',
            field=models.DateTimeField(verbose_name='回复时间'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='que_time',
            field=models.DateTimeField(verbose_name='提问时间'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='que_tittle',
            field=models.CharField(max_length=300, null=True, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='readcollect',
            name='read_date',
            field=models.DateTimeField(null=True, verbose_name='时间'),
        ),
    ]