from django.db import models
from .product import Products
from .customer import Customer
import datetime


class Order(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, help_text='This is the book title')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, help_text='This is the customer purchasing the book')
    quantity = models.IntegerField(default=1, help_text='This is the quantity of this partiuclar book purchased')
    price = models.FloatField(help_text='This is the price of one of this product')
    address = models.CharField (max_length=50, default='', blank=True,help_text='This is the customer address')
    phone = models.CharField (max_length=50, default='', blank=True, help_text='This is the customer phone number')
    date = models.DateField (default=datetime.datetime.today, help_text='This is the date the order was placed')
    status = models.BooleanField (default=False, help_text='Check this box to mark the order complete')

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')

    @staticmethod
    def get_order_by_book(customer_id, title):
        return Order.objects.filter(product__name=title,customer=customer_id).order_by('-date')