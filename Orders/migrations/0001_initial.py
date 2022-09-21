# Generated by Django 4.0.6 on 2022-09-21 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_UUID', models.UUIDField(auto_created=True)),
                ('product_list', models.TextField(blank=True, editable=False, null=True, verbose_name='Список товаров')),
                ('adress', models.TextField(blank=True, editable=False, null=True, verbose_name='Адрес клиента')),
                ('contacts', models.TextField(blank=True, editable=False, null=True, verbose_name='Контакты клиента')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')),
            ],
            options={
                'verbose_name': 'текущий заказ',
                'verbose_name_plural': 'Текущие заказы',
                'ordering': ('-created',),
            },
        ),
    ]
