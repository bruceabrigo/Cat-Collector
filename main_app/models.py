from django.db import models

# Create your models here.

# class INHERITANCE
# models.Model is being inherited from views
class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField() 

    # dunder method to return cat name
    def __str__(self):
        return self.name