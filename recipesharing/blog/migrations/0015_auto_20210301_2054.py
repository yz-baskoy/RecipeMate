# Generated by Django 3.0 on 2021-03-01 20:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0014_post_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='rate',
        ),
        migrations.AddField(
            model_name='post',
            name='rate',
            field=models.ManyToManyField(default=0, to=settings.AUTH_USER_MODEL),
        ),
    ]
