# Generated by Django 4.0.4 on 2022-04-29 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logi', '0016_auto_20220429_0123'),
    ]

    operations = [
        migrations.AddField(
            model_name='fish',
            name='fishPNG',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
