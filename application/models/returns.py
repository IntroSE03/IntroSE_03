from django.db import models
from .product import Products
from .customer import Customer
from .orders import Order
import datetime


class Return(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, help_text='This is the book title')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, help_text='This is the customer returning the book')
    quantity = models.IntegerField(default=1, help_text='This is the quantity of this partiuclar book being returned')
    price = models.FloatField(help_text='This is the price of one of this product')
    #address = models.CharField (max_length=50, default='', blank=True,help_text='This is the customer address')
    phone = models.CharField (max_length=50, default='', blank=True, help_text='This is the customer phone number')
    date = models.DateField (default=datetime.datetime.today, help_text='This is the date the return was placed')
    status = models.BooleanField (default=False, help_text='Check this box to mark the return complete')

    def placeReturn(self):
        self.save()

    @staticmethod
    def get_returns_by_customer(customer_id):
        return Return.objects.filter(customer=customer_id).order_by('-date')
