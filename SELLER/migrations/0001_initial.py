# Generated by Django 3.0.8 on 2020-10-10 10:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=150)),
                ('shop_email_address', models.EmailField(blank=True, max_length=254, null=True)),
                ('shop_phone_number', models.CharField(max_length=13)),
                ('shop_address', models.TextField()),
                ('area_pincode', models.CharField(max_length=6)),
                ('shop_state', models.CharField(max_length=200)),
                ('shop_city', models.CharField(max_length=200)),
                ('shop_description', models.TextField(blank=True, null=True)),
                ('is_shop_verified', models.BooleanField(default=False)),
                ('shop_owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tbl_registered_shops',
            },
        ),
        migrations.CreateModel(
            name='ShopOwnerBankDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=255)),
                ('account_number', models.CharField(max_length=20)),
                ('IFSC_code', models.CharField(max_length=11)),
                ('PAN_number', models.CharField(max_length=11)),
                ('shop_owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='SELLER.Shop')),
            ],
            options={
                'db_table': 'tbl_shop_owner_bank_details',
            },
        ),
    ]
