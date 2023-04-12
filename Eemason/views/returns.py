from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Products
from store.models.orders import Order
from store.middlewares.auth import auth_middleware
from store.models.returns import Return

class ReturnView(View):
    def get(self , request ):
        customer = request.session.get('customer')
        returns = Return.get_returns_by_customer(customer)
        print(returns)
        return render(request , 'returns.html'  , {'returns' : returns})

    def post(self, request):
        title = request.POST.get('title')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Products.get_products_by_title(title)
        order = Order.get_order_by_book(customer, title)
        print(phone, customer, order)

        for product in products:
            print(cart.get(str(product.id)))
            returns = Return(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          phone=phone,
                          quantity= order.values('quantity'))
            returns.save()
        request.session['returns'] = {}

        return redirect('returns')

