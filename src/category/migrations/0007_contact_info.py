# Generated by Django 3.1.4 on 2021-01-01 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0006_auto_20201231_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='info',
            field=models.TextField(null=True),
        ),
    ]
