# Generated by Django 3.0.7 on 2020-07-12 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20200712_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artisan',
            name='rating',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
