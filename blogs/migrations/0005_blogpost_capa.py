# Generated by Django 4.0 on 2021-12-28 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_rename_usuario_blogpost_proprietario'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='capa',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
