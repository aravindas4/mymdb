# Generated by Django 2.2.4 on 2019-09-02 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photograph',
            field=models.CharField(max_length=255, null=True, verbose_name='photograph'),
        ),
    ]
