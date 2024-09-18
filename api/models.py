from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class products(models.Model): #create a table named products,and inharits already existing models
# to it.when creating a table ,id is already created automatically.so no need of adding id
    name=models.CharField(unique=True,max_length=100)
    price=models.PositiveBigIntegerField()
    description=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    image=models.ImageField(upload_to='Image',null=True) #"null=True" means,we allow to add a product without image.
    #ie,image is null is also acceptable.
    def __str__(self): #it is a dendre method for getting an object into string format
        return self.name
    
class Carts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)#'on_delete=models.CASCADE' is used to delete
    product=models.ForeignKey(products,on_delete=models.CASCADE)#carted details when the user details 
                                                                #is deleted
    date=models.DateTimeField(auto_now_add=True)#if we put auto_now_add=True,product carted time is
                                                #automatically set.if it is False we set the time
                                                                 
class Reviews(models.Model):
    product=models.ForeignKey(products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])#the
    #minvalueValidator and maxvaluevalidators are used to set range
    comment=models.CharField(max_length=200)

    def __str__(self):
        return self.comment

