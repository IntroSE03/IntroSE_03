from django.db import models

class Category(models.Model):
    name= models.CharField(max_length=50, help_text='Enter the genre for this category of book, max 50 characters')
    

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name
