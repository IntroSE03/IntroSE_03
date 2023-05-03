from django.db import models

class Seller(models.Model):
    first_name = models.CharField(max_length=50, help_text='Enter first name, max 50 characters')
    last_name = models.CharField (max_length=50, help_text='Enter last name, max 50 characters')
    email=models.EmailField(help_text='Enter email in name@provider.com format')
    username=models.CharField(max_length=50, help_text='Enter Username, max 50 characters')

    #to save the data
    def register(self):
        self.save()


    @staticmethod
    def get_customer_by_email(email):
        try:
            return Seller.objects.get(email= email)
        except:
            return False


    def isExists(self):
        if Seller.objects.filter(email = self.email):
            return True

        return False

    def __str__(self):
        return self.email

class testSeller(models.Model):
    first_name = models.CharField(max_length=50, help_text='Enter first name, max 50 characters')
    last_name = models.CharField (max_length=50, help_text='Enter last name, max 50 characters')
    email=models.EmailField(help_text='Enter email in name@provider.com format')
    username=models.CharField(max_length=50, help_text='Enter Username, max 50 characters')

    def __init__(self,first_name,last_name,email,username):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username

    #to save the data
    def register(self):
        self.save()


    @staticmethod
    def get_customer_by_email(email):
        try:
            return Seller.objects.get(email= email)
        except:
            return False


    def isExists(self):
        if Seller.objects.filter(email = self.email):
            return True

        return False

    def __str__(self):
        return self.email

def test_seller(fname,lname,email,username):
    tseller = testSeller(fname,lname,email,username)
    tseller.first_name = fname
    tseller.last_name = lname
    tseller.email = email
    tseller.username = username
    return tseller
