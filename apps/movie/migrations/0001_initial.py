# Generated by Django 2.2.2 on 2019-07-03 03:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('created_by', models.CharField(blank=True, max_length=250, null=True)),
                ('modified_by', models.CharField(blank=True, max_length=250, null=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('plot', models.TextField(blank=True, verbose_name='plot')),
                ('date', models.DateField(blank=True, null=True, verbose_name='date')),
                ('runtime', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='runtime in mins')),
                ('webiste', models.URLField(blank=True, null=True, verbose_name='webiste')),
                ('rating', models.PositiveSmallIntegerField(choices=[(0, 'Not Rated'), (1, 'General Audiences'), (2, 'Parental Audiences'), (3, 'Restricted')], verbose_name='rating')),
            ],
            options={
                'verbose_name': 'Movie',
                'verbose_name_plural': 'Movies',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('created_by', models.CharField(blank=True, max_length=250, null=True)),
                ('modified_by', models.CharField(blank=True, max_length=250, null=True)),
                ('first_name', models.CharField(max_length=255, verbose_name='first name')),
                ('last_name', models.CharField(max_length=255, verbose_name='last name')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='date of birth')),
                ('died_on', models.DateField(blank=True, null=True, verbose_name='died on')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'Persons',
            },
        ),
        migrations.CreateModel(
            name='MoviePerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('created_by', models.CharField(blank=True, max_length=250, null=True)),
                ('modified_by', models.CharField(blank=True, max_length=250, null=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Movie')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Person')),
            ],
            options={
                'verbose_name': 'Movie Person',
                'verbose_name_plural': 'Movie Persons',
            },
        ),
        migrations.CreateModel(
            name='MovieImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('created_by', models.CharField(blank=True, max_length=250, null=True)),
                ('modified_by', models.CharField(blank=True, max_length=250, null=True)),
                ('path', models.CharField(max_length=255, verbose_name='image path')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Movie Image',
                'verbose_name_plural': 'Movie Images',
            },
        ),
    ]