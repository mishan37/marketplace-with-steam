# Generated by Django 2.0.3 on 2018-04-02 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_item_lot_transaction_user_inventory_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='level',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='money',
            field=models.IntegerField(null=True),
        ),
    ]