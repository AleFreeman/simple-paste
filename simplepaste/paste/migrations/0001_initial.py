# Generated by Django 3.1.4 on 2020-12-12 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PasteBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paste_box', models.CharField(max_length=2000)),
            ],
        ),
    ]
