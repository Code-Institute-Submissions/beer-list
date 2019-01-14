# Generated by Django 2.0.5 on 2019-01-14 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Brewery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=50)),
                ('town', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('notes', models.TextField(blank=True)),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')], default=3, verbose_name='Rating (stars)')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beer_review', to=settings.AUTH_USER_MODEL)),
                ('beer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='beer.Beer')),
            ],
            options={
                'ordering': ('beer', 'created'),
            },
        ),
        migrations.AddField(
            model_name='beer',
            name='brewery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beer.Brewery'),
        ),
        migrations.AddField(
            model_name='beer',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]