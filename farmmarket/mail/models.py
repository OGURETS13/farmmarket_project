from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_farmer = models.BooleanField(
        'Я фермер',
        default=False
    )
    email = models.EmailField(
        blank=False,
        unique=True,
    )


class Product(models.Model):
    name = models.CharField(
        max_length=256,
        null=False,
        blank=False
    )
    units = models.CharField(
        max_length=20,
        null=False,
        blank=False
    )
    price = models.FloatField()
    image = models.ImageField(
        null=True,
        blank=True,
        max_length=100,
        upload_to='media/images'
    )

    def __str__(self):
        return self.name


class OrderStatus(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('registered', 'Registered'),
        ('accepted', 'Accepted'),
        ('delivered', 'Delivered'),
        ('closed', 'Closed')
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        unique=True
    )

    def __str__(self) -> str:
        return self.status


class Order(models.Model):
    client = models.ForeignKey(
        User,
        related_name='orders_made',
        on_delete=models.CASCADE
    )
    farmer = models.ForeignKey(
        User,
        related_name='orders_received',
        on_delete=models.CASCADE
    )
    date = models.DateTimeField(
        auto_now_add=True,
        db_index=True
    )
    commentary = models.TextField(
        null=True,
        blank=True
    )
    address = models.TextField(
        null=False,
        blank=False
    )
    status = models.ForeignKey(
        OrderStatus,
        related_name='orders',
        on_delete=models.SET_DEFAULT,
        default=0
    )

    def __str__(self):
        return str(self.pk)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name='items',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        related_name='orders',
        on_delete=models.CASCADE
    )
    quantity = models.FloatField()

    def __str__(self) -> str:
        return f'order #{str(self.order.pk)}, {str(self.product.name)}',
