# Generated by Django 3.1.3 on 2020-11-24 18:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=150)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('stock', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product_picture', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]
