from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import products ,Carts
from api.serializers import productserializer,ProductModelSerializer,UserSerializer
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class productView(APIView):
    def get(self,request,*args,**kw):

        qs=products.objects.all()
        serializer=productserializer(qs,many=True)
        return Response(data=serializer.data)
    
    def post(self,request,*args,**kw):

        serializer=productserializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            products.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class productDetailView(APIView):


    def get(self,request,*args,**kw):
       print(kw)
       id=kw.get('id')
       qs=products.objects.get(id=id)
       serializer=productserializer(qs)
       return Response(data=serializer.data)
    
    def put(self,request,*args,**kw):
        serializer=productserializer(data=request.data)
        if serializer.is_valid():
            id=kw.get('id')
            products.objects.filter(id=id).update(**request.data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    
    
    def delete(self,request,*args,**kw):
        id=kw.get('id')
        products.objects.filter(id=id).delete()
        return Response(data='item deleted')

# class ProductViewsetView(ViewSet):
#     def list(self,request,*args,**kw):
#         qs=products.objects.all()
#         serializer=ProductModelSerializer(qs,many=True)
#         return Response(data=serializer.data)
    
#     def create(self,request,*args,**kw):
#         serializer=ProductModelSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)
        
    

    
#     def retrieve(self,request,*args,**kw):
#         id=kw.get('pk')
#         qs=products.objects.get(id=id)
#         serializer=ProductModelSerializer(qs)
#         return Response(data=serializer.data)
    
#     def destroy(self,request,*args,**kw):
#         id=kw.get('pk')
#         products.objects.filter(id=id).delete()
#         return Response(data='item deleted')
    
#     def update(self,request,*args,**kw):
#         id=kw.get('pk')
#         obj=products.objects.get(id=id)
#         serializer=ProductModelSerializer(data=request.data,isinstance=obj)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)
        
#     #custom method(categories is we created,its cannot exist in viewset)
#     @action(methods=['GET'],detail=False) #detail=False given for to get a perticular id informaton.
#     def categories(self,request,*args,**kw):

#         qs=products.objects.values_list('category',flat=True).distinct()#distinct used to show same 
           #category in one time
#         return Response(data=qs)
    

class UserView(ViewSet):
    def create(self,request,*args,**kw):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


class ProductViewsetView(ModelViewSet): #WE CAN DO THE HIDED CODE USING MODELVIEWSET.ALL THE FUNCTIONS
    serializer_class=ProductModelSerializer #WE CREATED ABOVE(HIDED) IS ALREADY IMPLEMENTED IN
    queryset=products.objects.all() #MODELVIEWSET.WE USE SAME CLASSNAME HERE SO NO NEED OF ADDING NEW 
                                    #URL
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]

    @action(methods=['GET'],detail=False) #detail=False given for to get a perticular id informaton.
    def categories(self,request,*args,**kw):
        qs=products.objects.values_list('category',flat=True).distinct()
        return Response(data=qs)
    
    @action(methods=['POST'],detail=True)
    def add_cart(self,request,*args,**kw):
        id=kw.get('pk')
        user=request.user
        item=products.objects.get(id=id)#here we serialization is not done because we add data already
        user.carts_set.create(product=item)#in the table not from the client side.
        return Response(data='item succesfully added to cart')

class UserView(ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()



class CartView(APIView):
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]

    def post(self,request,*args,**kw): 
        print(kw)
        id=kw.get('id')
        user=request.user
        item=products.objects.get(id=id)
        Carts.objects.create(product=item,user=user)
        return Response(data='item succesfully added to cart')




    

