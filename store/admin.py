from django.contrib import admin
from .models.product import Products
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from .models.returns import Return
from .models.seller import Seller

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'image', 'susFlag']
    list_filter = ['category', 'susFlag']
    search_fields = ['name']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'product', 'date', 'status']
    list_filter = ['customer', 'date', 'status']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['email','first_name','last_name','phone', 'susFlag']
    list_filter = ['email','first_name','last_name','phone', 'susFlag']

class ReturnAdmin(admin.ModelAdmin):
    list_display = ['customer', 'product', 'date', 'status']
    list_filter = ['customer', 'date', 'status']

class SellerAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'username']    
    
# Register your models here.
admin.site.register(Products,AdminProduct)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Return,ReturnAdmin)
admin.site.register(Seller,SellerAdmin)


# username = Tanushree, email = tanushree7252@gmail.com, password = 1234
