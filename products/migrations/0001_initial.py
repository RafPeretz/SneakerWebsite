# Generated by Django 4.0 on 2021-12-14 12:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('size', '0001_initial'),
        ('company', '0001_initial'),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sneakers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('description', models.TextField(blank=True)),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('is_published', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='category.category')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company.company')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='size.size')),
            ],
        ),
    ]
