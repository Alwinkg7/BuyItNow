# Generated by Django 5.0.6 on 2024-06-28 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(blank=True, max_length=100, null=True)),
                ('UserEmail', models.CharField(blank=True, max_length=100, null=True)),
                ('Userpassword', models.CharField(blank=True, max_length=100, null=True)),
                ('Usercpassword', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
