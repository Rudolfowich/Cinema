# Generated by Django 3.0.3 on 2020-02-25 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='youtube',
            field=models.URLField(default='https://www.youtube.com/embed/49s0cTx2C4M', null=True),
        ),
    ]
