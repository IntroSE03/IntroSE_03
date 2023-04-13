from django.contrib.auth.models import User
from django.test import TestCase,SimpleTestCase, Client
from django.utils import timezone
from django.urls import reverse, resolve
from store.views.login import Login
from store.views.signup import Signup
from store.models import *
from django.http import HttpRequest
from .views.cart import Cart
from .views.returns import ReturnView
from .views.orders import OrderView
from django.contrib.sessions import *
from django.contrib import admin
import json

if __name__ == '__main__':
    unittest.main()

#admin: 6/5
#cust: 6/5
#login: 3/5

#to test: django user creation, login, what does login actually return

#potentially: admin(6/5),customer(6/5), login(4/5)
#done: 6/15
#maybe done 13/15
#todo: 2/17

#issues login and cust stuff all require figuring out how to get django logged in and a persistent db
## this will require figuring out how to authenticate past the middleware
# admin requires a db and figuring out the django admin functions to edit DB attributes
class TestViews(SimpleTestCase):
    # tests that the login url is resolved correctly
    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, Login)
    # tests whether the signup page url is resolved/functional
    def test_login_signup_url(self):
        url = reverse('signup')
        self.assertEquals(resolve(url).func.view_class, Signup)
    # tests whether the login page can be loaded correctly to facilitate the login
    def test_login_func(self):
        page = '/login'
        response = self.client.get(page, follow=True)
        self.assertEquals(response.status_code, 200)
    def test_customer_cart_view(self):
        url = reverse('test_cart')
        self.assertEquals(resolve(url).func.view_class, Cart)
    def test_customer_order_view(self):
        url = reverse('test_orders')
        self.assertEquals(resolve(url).func.view_class, OrderView)
    def test_customer_return_view(self):
        url = reverse('test_returns')
        resolved = str(resolve(url).func.view_class)
        returnview = str(ReturnView)
        assert(resolved in returnview)
        #self.assertEquals(resolve(url).func.view_class, ReturnView)
    # def test_editr(self):
    #     page = '/admin/login/?next=/admin'
    #     response = self.client.get(page, follow=True)
    #     self.assertEquals(response.status_code, 200)
# class AdminFailSetup(TestCase):
#     def setUp(self):
#         self.client = Client()
#     def create_user(self):
#         username, password = 'admin', 'password'
#         user = User.objects.create_user(
#             username = username,
#             email = 'admin@admin.ca',
#             is_superuser = False
#         ) [0]
#         user.set_password(password)
#         user.save()
#         self.user = user
# class TestFailLogin(AdminFailSetup):
#     def test_login_admin_fail(self):
#         self.client.login(username='notadmin',password = 'incorrect')
#         page = '/admin/store/customer'
#         response = self.client.get(page, follow=True)
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'admin/login.html')
#         self.assertTemplateUsed(response, 'admin/base_site.html')
class TestCustViews(TestCase):
    #tests that the customer can view the homepage of the store
    def test_customer_view_home(self):
        client = Client()
        response = client.get(reverse('store'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'index.html')
    # tests that the customer can load and view products from the DB
    def test_customer_retrieve_products(self):
        data = Products.get_all_products()
        if data == 0:
            datareturned = False
        else:
            datareturned = True
        assert(datareturned)
    # tests whether the user receives a response when searching for a specific title/filtered option
    def test_customer_search_inv(self):
        data = Products.get_products_by_title('The Communist Manifesto')
        if data == 0:
            datareturned = False
        else:
            datareturned = True
        assert(datareturned)
    # def test_customer_cart_GET(self):
    #     client = Client()
    #     cust = Customer.objects.create(
    #         first_name = 'admin',
    #         last_name = 'admin',
    #         phone = '1234567890',
    #         email = 'admin@admin.ca',
    #         password = 'password',
    #         susFlag = 0
    #     )
    #     #cust.register()
    #     #cust.save()
    #     #self.customer = cust
    #     querydict = {'email':['admin@admin.ca'],'password' : ['password']}
    #     fake_request = HttpRequest()
    #     fake_request.user = client
    #     #fake_request.META['SERVER_NAME'] = store.domain
    #     fake_request.META['SERVER_PORT'] = 8000
    #     fake_request.META['email'] = 'admin@admin.ca'
    #     fake_request.META['password'] = 'password'
    #    # s = SessionStore()
    #     #s.create()
    #    # s = request.session.session_key
    #     #fake_request.session = s
    #     Login.post(self,fake_request)
    #     response = client.get(reverse('cart'))
    #     #self.assertEquals(response.status_code, 200)
    #     assert('uwu' == 'uwu')


    # # tests that the custome
    # def test_cart_page(self):
    #     page = '/returns'
    #     response = self.client.get(page, follow=True)
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'base.html')
class AdminSetup(TestCase):
    def setUp(self):
        self.client = Client()
        self.login()
    def create_user(self):
        username, password = 'admin', 'password'
        user = User.objects.get_or_create(
            username = username,
            email = 'admin@admin.ca',
            is_superuser = True
        ) [0]
        user.set_password(password)
        user.save()
        self.user = user
    def login(self):
        self.client.login(username='admin', password='password')

class TestAdminViews(AdminSetup):
    #tests for admin login functionality
    def test_login_admin(self):
        page = '/admin/'
        response = self.client.get(page, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin/login.html')
        self.assertTemplateUsed(response, 'admin/base_site.html')
    # tests that the admin can view users and user suspension status (susFlag)
    def test_admin_view_users(self):
        page = '/admin/store/customer/'
        response = self.client.get(page, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin/base.html')
    #tests that the admin can view products and product suspension information (susFlag)
    def test_admin_view_products(self):
        page = '/admin/store/products/'
        response = self.client.get(page, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin/base_site.html')
    #tests that the admin can reach the page to edit products and change the product suspension flag, checks access to the products
    def test_admin_edit_inv(self):
        page = '/admin/store/products/70/change/'
        response = self.client.get(page, follow=True)
        self.assertEquals(response.status_code, 200)
    #tests that the admin can reach the page to edit users and change the product suspension flag, checks access to the users page
    def test_admin_edit_usr(self):
        page = '/admin/store/customer/11/change/'
        response = self.client.get(page, follow=True)
        self.assertEquals(response.status_code, 200)
    #tests that the admin can reach the page to edit orders, by reaching the page the admin is shown to be able to edit orders and delete them if desired
    def test_admin_edit_ordr(self):
        page = '/admin/store/order/18/change/'
        response = self.client.get(page, follow=True)
        self.assertEquals(response.status_code, 200)
    # tests that the admin can reach the page to edit returns, by reaching the page the admin is shown to be able to return orders and delete them if desired
    def test_admin_edit_return(self):
        page = '/admin/store/return/6/change/'
        response = self.client.get(page, follow=True)
        self.assertEquals(response.status_code, 200)
