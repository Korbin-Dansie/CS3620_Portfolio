# Generated by Django 4.2.5 on 2023-10-10 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_contact_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobby',
            name='image',
            field=models.ImageField(max_length=255, upload_to='hobby'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(upload_to='portfolio'),
        ),
    ]