# Generated by Django 4.1.2 on 2022-11-01 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_blog_video_portfolio_video_alter_blog_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='portfolios'),
        ),
    ]
