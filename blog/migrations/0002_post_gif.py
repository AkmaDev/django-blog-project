# Generated by Django 4.2.7 on 2023-11-12 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='gif',
            field=models.ImageField(blank=True, null=True, upload_to='gifs/'),
        ),
    ]
