# Generated by Django 2.2.12 on 2020-06-19 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover',
            field=models.ImageField(default='1.jpeg', upload_to='images/'),
            preserve_default=False,
        ),
    ]
