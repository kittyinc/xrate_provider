# Generated by Django 3.2 on 2022-01-17 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rates', '0005_auto_20220117_0818'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='variant_name',
            field=models.CharField(default='default', max_length=25),
        ),
    ]
