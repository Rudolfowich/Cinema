# Generated by Django 3.0.3 on 2020-02-27 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sum_all',
            field=models.IntegerField(blank=True, default='0'),
        ),
    ]