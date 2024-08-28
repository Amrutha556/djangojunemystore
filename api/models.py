from django.db import models

# Create your models here.
class products(models.Model): #create a table named products,and inharits already existing models
# to it.when creating a table ,id is already created automatically.so no need of adding id
    name=models.CharField(unique=True,max_length=100)
    price=models.PositiveBigIntegerField()
    description=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    image=models.ImageField(null=True) #"null=True" means,we allow to add a product without image.
    #ie,image is null is also acceptable.
    def __str__(self): #it is a dendre method for getting an object into string format
        return self.name


