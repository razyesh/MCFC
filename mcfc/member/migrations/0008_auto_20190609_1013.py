# Generated by Django 2.1.7 on 2019-06-09 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0007_auto_20190609_1007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='members',
            name='url_height',
        ),
        migrations.RemoveField(
            model_name='members',
            name='url_width',
        ),
        migrations.AlterField(
            model_name='members',
            name='image',
            field=models.ImageField(default='member/images/propic.png', upload_to='member/images'),
        ),
    ]
