from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers
from . import models

from .forms import RentForm

# Create your views here.

class RentApi(APIView):
    """Test API View."""

    def post(self, request):
        """Create a hello message with our name."""
        serializer = serializers.RentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)  # serializer.data döndürülüyor
        return Response(serializer.errors, status=400)
    
    def get(self, request, id = None):
        if id:
            item = models.Rent.objects.get(id=id)
            serializer = serializers.RentSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = models.Rent.objects.all()
        serializer = serializers.RentSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
    def delete(self, request, id=None):
        item = models.Rent.objects.filter(id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})
    
    def patch(self, request, id=None):
        item = models.Rent.objects.get(id=id)
        serializer = serializers.RentSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        

def addRent(request):  
    if request.method == "POST":  
        form = RentForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/api/rent-list')  
            except:  
                pass 
    else:  
        form = RentForm()  
    return render(request,'rent.html',{'form':form}) 

def rentList(request):
    
    rents = models.Rent.objects.all()
    return render(request,"listRents.html",{'rents':rents})  


def edit(request, id):  
    rents = models.Rent.objects.get(id=id) 

    return render(request,'editRent.html', {'rents':rents}) 

def update(request, id):  
    rents = models.Rent.objects.get(id=id)  
    form = RentForm(request.POST, instance = rents)  
    if form.is_valid():  
        form.save()  
        return redirect("/api/rent-list")  
    return render(request, 'editRent.html', {'rents': rents})  

def destroy(request, id):  
    rents = models.Rent.objects.get(id=id)  
    rents.delete()  
    return redirect("/api/rent-list")  
