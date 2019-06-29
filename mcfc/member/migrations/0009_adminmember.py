# Generated by Django 2.2.2 on 2019-06-29 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0008_auto_20190609_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=5)),
                ('image', models.ImageField(default='member/images/propic.png', upload_to='member/admin/images')),
                ('name', models.CharField(max_length=20)),
                ('contact_no', models.CharField(max_length=10)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'admin_member',
            },
        ),
    ]
