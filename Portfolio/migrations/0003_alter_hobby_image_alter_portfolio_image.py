# Generated by Django 4.2.5 on 2023-10-09 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_hobby_image_alter_portfolio_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobby',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='hobby'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='portfolio'),
        ),
    ]
