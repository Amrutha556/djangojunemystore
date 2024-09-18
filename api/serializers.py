
from rest_framework import serializers
from api.models import products,Carts
from django.contrib.auth.models import User



class productserializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)#read_only=True is given to do only serialization.
    name=serializers.CharField()
    price=serializers.IntegerField()
    description=serializers.CharField()
    category=serializers.CharField()
    image=serializers.ImageField(required=False,default=None) 
    #we dont put any image in this project.but a place is 
    #alloted for image.so in the time of data updation ,error occurs.
    # to avoid that 'read_only=True' is given
    #required=false and default=none are used for to accept without image also

class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=products
        fields="__all__" # all fields get serialized
        #field=["name","price","description"]#only this field serialized


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password"]

    def create(self, validated_data):
        return User.objects.create_user(**self.validated_data)

class CartSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    user=serializers.CharField(read_only=True)
    product=serializers.CharField(read_only=True)
    date=serializers.CharField(read_only=True)#here all are in charfield,because there is no need of 
    #desrialization(no datas coming from client side)
    class Meta:
        model=Carts
        fields="__all__"
