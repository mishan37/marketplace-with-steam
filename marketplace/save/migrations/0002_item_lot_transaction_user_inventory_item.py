# Generated by Django 2.0.3 on 2018-03-15 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('starting_price', models.IntegerField()),
                ('type_item', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_code', models.IntegerField()),
                ('lot_name', models.CharField(max_length=30)),
                ('cost', models.IntegerField()),
                ('user_seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.User')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lot_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='marketplace.Lot')),
                ('user_buyer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.User')),
            ],
        ),
        migrations.CreateModel(
            name='User_Inventory_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('item_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.Item')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.User')),
            ],
        ),
    ]
