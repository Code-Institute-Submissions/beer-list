# Generated by Django 2.0.5 on 2019-01-15 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beer', '0002_auto_20190115_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='strength',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
    ]