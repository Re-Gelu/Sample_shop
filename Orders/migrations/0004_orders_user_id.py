# Generated by Django 4.1.1 on 2022-10-06 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0003_alter_orders_uuid_alter_orders_adress_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='user_id',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
    ]
