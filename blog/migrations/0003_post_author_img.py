# Generated by Django 2.0.7 on 2018-08-20 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180820_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author_img',
            field=models.ImageField(blank=True, null=True, upload_to='autor_images/'),
        ),
    ]