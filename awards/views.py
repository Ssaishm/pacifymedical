from django.shortcuts import render
from awards.models import Awards
from awards.models import Image
from django.http import Http404
from .serializers import AwardsSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.urlpatterns import format_suffix_patterns


@api_view(['GET', 'POST']) 
def awards_list(request):

    if request.method == 'GET':
        awards= Awards.objects.all()
        serializer = AwardsSerializer(awards, many =True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer =AwardsSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
       

@api_view(['GET','PUT','DELETE']) 
def awards_detail(request,id):
    try:
        awards=Awards.objects.get(pk=id)
    except Awards.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)       

    if request.method == 'GET':
           serializer =AwardsSerializer(awards)
           return Response(serializer.data)
    elif request.method == 'PUT':
         serializer =AwardsSerializer(awards,data= request.data)
         if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method =='DELETE':
        awards.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    ############################

def image(request,image_id): 
    if image is not None:
        return render(request, 'images/image.html',{'image':image})
    else:
        raise Http404('Image does not exist')
      
    

    
