# Generated by Django 3.2.9 on 2021-11-26 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learningportal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='video',
            field=models.FileField(blank=True, upload_to='videos/'),
        ),
    ]
