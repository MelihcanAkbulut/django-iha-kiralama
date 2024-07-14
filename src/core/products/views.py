
from django.shortcuts import render, redirect  
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
from .forms import ProductForm

from . import serializers
from . import models

# Create your views here.

class ProductApi2(viewsets.ModelViewSet):
    """Test API View."""
    serializer_class = serializers.ProductSerializer
    queryset = models.Products.objects.all()
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)

def productList(request):
    
    products = models.Products.objects.all()
    return render(request,"productList.html",{'products':products})  

class ProductApi(APIView):
    """Test API View."""

    def post(self, request):
        """Create a hello message with our name."""
        serializer = serializers.ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)  # serializer.data döndürülüyor
        return Response(serializer.errors, status=400)

        serializer = serializers.ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = serializer.save()
        return Response({
            serializer.data
        })
    
    def get(self, request, id = None):
        if id:
            item = models.Products.objects.get(id=id)
            serializer = serializers.ProductSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = models.Products.objects.all()
        serializer = serializers.ProductSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
    def delete(self, request, id=None):
        item = models.Products.objects.filter(id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})
    
    def patch(self, request, id=None):
        item = models.Products.objects.get(id=id)
        serializer = serializers.ProductSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
def addnew(request):  
    if request.method == "POST":  
        form = ProductForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/api/product-list')  
            except:  
                pass 
    else:  
        form = ProductForm()  
    return render(request,'addProduct.html',{'form':form})  

def edit(request, id):  
    product = models.Products.objects.get(id=id)  
    return render(request,'editProduct.html', {'product':product}) 

def update(request, id):  
    product = models.Products.objects.get(id=id)  
    form = ProductForm(request.POST, instance = product)  
    if form.is_valid():  
        form.save()  
        return redirect("/api/product-list")  
    return render(request, 'editProduct.html', {'product': product})  

def destroy(request, id):  
    employee = models.Products.objects.get(id=id)  
    employee.delete()  
    return redirect("/api/product-list")  