# Generated by Django 3.2.9 on 2021-11-14 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='movie',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
