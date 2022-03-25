# Generated by Django 4.0.3 on 2022-03-24 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('memeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='comments_number',
            field=models.IntegerField(blank='True', default=0, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='likes_number',
            field=models.IntegerField(blank='True', default=0, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
