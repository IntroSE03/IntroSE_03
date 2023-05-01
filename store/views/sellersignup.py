from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.seller import Seller
from django.views import View


class Sellersignup (View):
    def get(self, request):
        return render (request, 'sellersignup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get ('firstname')
        last_name = postData.get ('lastname')
        email = postData.get ('email')
        username = postData.get ('username')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'username': username
        }
        error_message = None

        seller = Seller (first_name=first_name,
                             last_name=last_name,
                             email=email,
                             username=username)
        error_message = self.validateSeller (seller)

        if not error_message:
            print (first_name, last_name, email, username)
            seller.register ()
            return redirect ('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render (request, 'sellersignup.html', data)

    def validateSeller(self, seller):
        error_message = None
        if (not seller.first_name):
            error_message = 'Please Enter your First Name'
        elif len (seller.first_name) < 3:
            error_message = 'First Name must be 3 char long or more'
        elif not seller.last_name:
            error_message = 'Please Enter your Last Name'
        elif len (seller.last_name) < 3:
            error_message = 'Last Name must be 3 char long or more'
        elif len (seller.email) < 5:
            error_message = 'Email must be 5 char long'
        elif seller.isExists ():
            error_message = 'Email Address Already Registered..'
        # saving

        return error_message
