from django.db import models
from utils.model_abstracts import Model
from django_extensions.db.models import (
	TimeStampedModel, 
	ActivatorModel,
	TitleDescriptionModel
)

class Home(models.Model):
    
    title =models.CharField(max_length=200)
    outlet = models.CharField(default=' ',null= True,max_length=100)
    news = models.TextField(blank=False, null=True,max_length=6000,verbose_name="News")


    class Meta:
        verbose_name_plural = "HomeNews"

    def __str__(self):
        return self.title + ' ' + self.outlet+' '+self.news
    

class Hblogs(models.Model):
    
    heading =models.CharField(max_length=200)
    author = models.CharField(default='Pacify Medical Technologies ',null=True,max_length=100)
    blogs = models.TextField(blank=False, null=True,max_length=6000,verbose_name="Blogs")

    class Meta:
        verbose_name_plural = "Homeblogs"

    def __str__(self):
        return self.heading + ' ' + self.author+' '+self.blogs
    
class Image(models.Model):
    name= models.CharField(max_length=200)
    image =models.ImageField(upload_to='awards/files/covers')