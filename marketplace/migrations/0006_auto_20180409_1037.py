# Generated by Django 2.0.2 on 2018-04-09 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0005_auto_20180409_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='lot_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='marketplace.Lot'),
        ),
    ]