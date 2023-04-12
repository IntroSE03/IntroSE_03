from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50, help_text='Enter first name, max 50 characters')
    last_name = models.CharField (max_length=50, help_text='Enter last name, max 50 characters')
    phone = models.CharField(max_length=10, help_text='Enter phone number, do not include hyphens')
    email=models.EmailField(help_text='Enter email in name@provider.com format')
    password = models.CharField(max_length=100, help_text='Enter password (in encrypted form)')
    susFlag = models.IntegerField(default=1, help_text='Set this to 0 for unsuspended, 1 for suspended')

    #to save the data
    def register(self):
        self.save()


    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email= email)
        except:
            return False


    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return False

    def __str__(self):
        return self.email


