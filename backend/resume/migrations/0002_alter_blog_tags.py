# Generated by Django 4.1.2 on 2022-10-31 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(related_name='tags', to='resume.tag'),
        ),
    ]