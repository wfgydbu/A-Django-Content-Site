# Generated by Django 2.0.6 on 2018-06-09 21:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sticker', '0002_auto_20180609_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='sticker',
            name='md5',
            field=models.CharField(default=django.utils.timezone.now, max_length=32),
            preserve_default=False,
        ),
    ]