# Generated by Django 3.1.4 on 2020-12-13 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paste', '0002_pastebox_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='pastebox',
            name='paste_title',
            field=models.CharField(default='old_title', max_length=30),
            preserve_default=False,
        ),
    ]
