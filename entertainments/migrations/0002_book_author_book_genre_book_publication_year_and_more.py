# Generated by Django 4.2.2 on 2023-06-29 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entertainments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='publication_year',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='movie',
            name='release_year',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='progress',
            name='status',
            field=models.CharField(choices=[('favorite', 'Favorite'), ('watching_reading', 'Watching/Reading'), ('completed', 'Completed'), ('abandoned', 'Abandoned')], default='watching_reading', max_length=20),
        ),
        migrations.AddField(
            model_name='tvseries',
            name='director',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tvseries',
            name='genre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tvseries',
            name='rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='tvseries',
            name='release_year',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
