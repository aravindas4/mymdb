# Generated by Django 2.2.4 on 2019-09-02 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='vote',
            constraint=models.UniqueConstraint(fields=('movie', 'user', 'vote'), name='unique_voting'),
        ),
    ]
