# Generated by Django 5.0.3 on 2024-03-12 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='img',
            field=models.ImageField(default=1, upload_to=''),
        ),
    ]
