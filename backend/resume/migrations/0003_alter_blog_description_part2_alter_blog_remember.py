# Generated by Django 4.1.2 on 2022-10-31 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_alter_blog_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description_part2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='remember',
            field=models.TextField(blank=True, null=True),
        ),
    ]
