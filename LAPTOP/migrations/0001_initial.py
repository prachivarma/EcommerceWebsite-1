# Generated by Django 3.0.8 on 2020-10-11 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('PRODUCTS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LaptopDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('laptop_type', models.CharField(choices=[('Notebook', 'Notebook'), ('Chromebook', 'Chromebook'), ('MacBook', 'MacBook'), ('Gaming Laptop', 'Gaming Laptop')], max_length=50)),
                ('RAM', models.IntegerField(default=1)),
                ('hdd', models.IntegerField(default=32)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='PRODUCTS.Product')),
            ],
            options={
                'verbose_name_plural': 'Laptop',
            },
        ),
    ]
