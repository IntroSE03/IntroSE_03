from django.contrib import admin
from django.urls import path
from .views.home import Index , store
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .views.returns import ReturnView
from .middlewares.auth import  auth_middleware
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

from .views.searchbar import search


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('returns', auth_middleware(ReturnView.as_view()), name='returns'),
    path('search/', search, name='searchbar'),
    path('test_cart', Cart.as_view(), name='test_cart'),
    path('test_orders', OrderView.as_view(), name='test_orders'),
    path('test_returns', ReturnView.as_view(), name='test_returns')

]
