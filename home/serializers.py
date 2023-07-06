
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from .models import Home
from .models import Hblogs
from rest_framework.fields import CharField




class HomeSerializer(serializers.ModelSerializer):
    title = CharField( required=True)
    news = CharField( required=True)
    outlet= CharField(required= True)
  
    class Meta:
        model =Home
        
        fields =('id','title','outlet','news')


class HblogsSerializer(serializers.ModelSerializer):
    heading = CharField( required=True)
    blogs = CharField( required=True)
    author= CharField(required= False)
  
    class Meta:
        model =Hblogs
        
        fields =('id','heading','author','blogs')
        