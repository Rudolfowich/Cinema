# Generated by Django 3.0.3 on 2020-02-25 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_auto_20200225_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to='review/'),
        ),
    ]
