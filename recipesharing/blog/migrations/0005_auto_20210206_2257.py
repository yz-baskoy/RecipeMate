# Generated by Django 3.0 on 2021-02-06 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210206_2254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredients',
            name='year_in_school',
        ),
        migrations.AddField(
            model_name='ingredients',
            name='ingredients',
            field=models.CharField(choices=[('easy', 'EASY'), ('middle', 'MIDDLE'), ('hard', 'HARD')], default='tomato', max_length=6),
        ),
    ]
