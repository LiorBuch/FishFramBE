# Generated by Django 4.0.4 on 2022-04-30 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logi', '0018_fish_imagecounty'),
    ]

    operations = [
        migrations.AddField(
            model_name='fish',
            name='sclaeHeight',
            field=models.FloatField(default=1),
        ),
        migrations.AddField(
            model_name='fish',
            name='sclaeWidth',
            field=models.FloatField(default=1),
        ),
    ]
