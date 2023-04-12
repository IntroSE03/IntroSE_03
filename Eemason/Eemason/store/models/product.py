from django.db import models
from .category import Category
class Products(models.Model):
    name = models.CharField(max_length=60, help_text='Enter book Title, max 60 characters')
    ISBN = models.CharField(max_length=14, default='', help_text='Enter ISBN in ###-########## format.')
    author = models.CharField(max_length=60, default='', help_text='Enter author name, max 60 characters')
    publisher = models.CharField(max_length=60, default='', help_text='Enter publisher name, max 60 characters')
    pubYear = models.IntegerField(default=0, help_text='Enter publication year (Example: 2023)')
    price= models.FloatField(default=0.0, help_text='Enter price in float format (Example: 69.69)')
    category= models.ForeignKey(Category,on_delete=models.CASCADE,default=1, help_text='Enter author name, max 60 characters' )
    description= models.CharField(max_length=250, default='', blank=True, null= True,
                                  help_text='Enter a description of the book, (Example: a summary)')
    image= models.ImageField(upload_to='uploads/products/', help_text='Upload an image of the book cover (for display)')
    susFlag = models.IntegerField(default=1, help_text='Set this to 0 for unsuspended, 1 for suspended')

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.exclude(susFlag=1).filter (id__in=ids)
    @staticmethod
    def get_all_products():
        return Products.objects.exclude(susFlag=1).all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Products.objects.exclude(susFlag=1).filter (category=category_id)
        else:
            return Products.get_all_products();

    @staticmethod
    def get_products_by_title(name):
        return Products.objects.filter(name=name)


    def __str__(self):
        return self.name