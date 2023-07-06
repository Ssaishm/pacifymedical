from .models import Home
from .models import Hblogs
from .serializers import HomeSerializer
from .serializers import HblogsSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.urlpatterns import format_suffix_patterns
from django.shortcuts import render
from home.models import Image
from django.http import Http404


@api_view(['GET', 'POST']) 
def home_list(request):

    if request.method == 'GET':
        home= Home.objects.all()
        serializer = HomeSerializer(home, many =True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer =HomeSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
       

@api_view(['GET','PUT','DELETE']) 
def home_detail(request,id):
    try:
        home=Home.objects.get(pk=id)
    except Home.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)       

    if request.method == 'GET':
           serializer = HomeSerializer(home)
           return Response(serializer.data)
    elif request.method == 'PUT':
         serializer = HomeSerializer(home,data= request.data)
         if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method =='DELETE':
        home.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST']) 
def hblogs_list(request):

    if request.method == 'GET':
        hblogs= Hblogs.objects.all()
        serializer = HblogsSerializer(hblogs, many =True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer =HblogsSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
       

@api_view(['GET','PUT','DELETE']) 
def hblogs_detail(request,id):
    try:
        hblogs=Hblogs.objects.get(pk=id)
    except Home.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)       

    if request.method == 'GET':
           serializer = HblogsSerializer(hblogs)
           return Response(serializer.data)
    elif request.method == 'PUT':
         serializer = HblogsSerializer(hblogs,data= request.data)
         if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method =='DELETE':
        hblogs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


@api_view(['GET', 'POST']) 
def home_list(request):

    if request.method == 'GET':
        home= Home.objects.all()
        serializer = HomeSerializer(home, many =True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer =HomeSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
       
@api_view(['GET','PUT','DELETE']) 
def home_detail(request,id):
    try:
        home=Home.objects.get(pk=id)
    except Home.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)       

    if request.method == 'GET':
           serializer = HomeSerializer(home)
           return Response(serializer.data)
    elif request.method == 'PUT':
         serializer = HomeSerializer(home,data= request.data)
         if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method =='DELETE':
        home.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
    
def image(request,image_id): 
    if image is not None:
        return render(request, 'images/image.html',{'image':image})
    else:
        raise Http404('Image does not exist')