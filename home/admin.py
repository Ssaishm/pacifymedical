from django.contrib import admin
from .models import Home 
from .models import Hblogs
from .models import Image


@admin.register(Home)
class homeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','outlet','news')

@admin.register(Hblogs)
class homeAdmin(admin.ModelAdmin):
    list_display = ('id', 'heading','author','blogs')

class ImageAdmin(admin.ModelAdmin):
    readonly_fields=('id',)
admin.site.register(Image,ImageAdmin)


