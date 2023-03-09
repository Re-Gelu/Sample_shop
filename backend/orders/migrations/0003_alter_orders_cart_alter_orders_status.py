# Generated by Django 4.0.8 on 2023-03-05 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_orders_order_uuid_alter_orders_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='cart',
            field=models.JSONField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.TextField(blank=True, choices=[('CREATED', 'Платеж создан'), ('WAITING', 'Платёж в обработке / ожидает оплаты'), ('PAID', 'Платёж оплачен'), ('EXPIRED', 'Время жизни счета истекло. Счет не оплачен.'), ('REJECTED', 'Платёж отклонен')], default='CREATED', null=True, verbose_name='Статус заказа'),
        ),
    ]
