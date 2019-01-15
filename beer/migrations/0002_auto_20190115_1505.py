# Generated by Django 2.0.5 on 2019-01-15 15:05

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('beer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='category',
            field=models.ManyToManyField(blank=True, help_text='Select a category for this beer', to='beer.Category'),
        ),
        migrations.AlterField(
            model_name='beer',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='eg. IPA, Golden, Craft', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='brewery',
            name='country',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, help_text='Enter a category (e.g. Ale)', max_length=200),
        ),
    ]
