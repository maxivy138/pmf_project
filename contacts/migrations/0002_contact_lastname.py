# Generated by Django 2.2.1 on 2019-05-30 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='lastname',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
