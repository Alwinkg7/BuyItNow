# Generated by Django 5.0.6 on 2024-06-24 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_categorydb',
            name='City',
        ),
        migrations.RemoveField(
            model_name='add_categorydb',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='add_categorydb',
            name='Gender',
        ),
        migrations.RemoveField(
            model_name='add_categorydb',
            name='Password',
        ),
        migrations.AddField(
            model_name='add_categorydb',
            name='Picture',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/'),
        ),
    ]
