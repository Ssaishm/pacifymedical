from django.contrib import admin
from .models import Image
from .models import Awards


@admin.register(Awards)
class AwardsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','details')


class ImageAdmin(admin.ModelAdmin):
    readonly_fields=('id',)
admin.site.register(Image,ImageAdmin)
