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


