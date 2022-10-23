from django.db import models

# Create your models here.
class About(models.Model): #converts the class into a model
    #id is authomatically generated 
    name = models.CharField(max_length=50) #charfield for 'str' type
    details = models.CharField(max_length=500)
    
    