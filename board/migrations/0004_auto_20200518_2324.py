# Generated by Django 3.0.6 on 2020-05-18 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_content_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='file',
            field=models.FileField(null=True, upload_to='documents/%Y.%m'),
        ),
    ]