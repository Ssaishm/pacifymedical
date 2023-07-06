from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from .models import Awards
from rest_framework.fields import CharField




class AwardsSerializer(serializers.ModelSerializer):
    title = CharField( required=True)
    details= CharField( required=True)
    
  
    class Meta:
        model =Awards
        
        fields =('id','title','details')