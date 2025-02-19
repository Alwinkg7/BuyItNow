# Generated by Django 5.0.6 on 2024-06-24 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_remove_add_categorydb_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='productcategorydb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cname', models.CharField(blank=True, max_length=100, null=True)),
                ('Pname', models.CharField(blank=True, max_length=100, null=True)),
                ('Quantity', models.IntegerField(blank=True, null=True)),
                ('Price', models.FloatField(blank=True, null=True)),
                ('Description', models.CharField(blank=True, max_length=100, null=True)),
                ('Pimage', models.ImageField(blank=True, null=True, upload_to='pictures/')),
            ],
        ),
    ]
