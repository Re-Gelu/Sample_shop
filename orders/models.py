from django.db import models
from django.utils import timezone
from shortuuid.django_fields import ShortUUIDField
import datetime

class orders(models.Model):
    
    user_id = models.PositiveIntegerField(
        editable=False,
    )

    UUID = ShortUUIDField(
        auto_created=True, 
        alphabet="0123456789",
        unique=True,
        verbose_name="UUID заказа",
        length=10,
        max_length=10,
        editable=False,
    )

    product_info = models.TextField(
        blank=True, null=True,
        verbose_name="Список товаров",
    )

    adress = models.TextField(
        blank=True, null=True,
        verbose_name="Адрес клиента",
    )

    contacts = models.TextField(
        blank=True, null=True,
        verbose_name="Контакты клиента",
    )

    created = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Дата создания заказа"
    )
    
    updated = models.DateTimeField(
        auto_now=True, 
        verbose_name="Дата обновления заказа"
    )
    
    cart = models.JSONField(
        editable=False,
    )
    
    class PaymentStatuses(models.TextChoices):
        CREATED = "CREATED", "Платеж создан"
        WAITING = "WAITING", "Платёж в обработке / ожидает оплаты"
        PAID = "PAID", "Платёж оплачен"
        EXPIRED = "EXPIRED", "Время жизни счета истекло. Счет не оплачен."
        REJECTED = "REJECTED", "Платёж отклонен"
    
    status = models.TextField(     
        choices=PaymentStatuses.choices,
        default=PaymentStatuses.CREATED,
        verbose_name="Статус заказа"
    )
    
    def expire_time(self):
        return self.created >= timezone.now() - datetime.timedelta(days=7)

    def __str__(self):
        return f' Заказ №: {self.id}, UUID: {self.UUID}'
    
    def save(self, *args, **kwargs):
        self.updated = timezone.now()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'текущий заказ'
        verbose_name_plural = 'Текущие заказы'
        ordering = ('-created',)