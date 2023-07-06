from django.urls import path
from django.contrib import admin
from awards import views as awards_views 
from core import views as core_views
from demo import views as demo_views
from distribution import views as distribution_views
from careers import views as careers_views
from home import views as home_views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    #path('contact/', core_views.ContactAPIView.as_view()),
    path('api-token-auth/', obtain_auth_token), #gives us access to token auth
    path('democontact/', demo_views.DemoContactAPIView.as_view()),
    path('wcontact/', core_views.wContactAPIView.as_view()),
    path('discontacts/', distribution_views.disContactAPIView.as_view()),
    path('careers/', careers_views.careers_list),
    path('careers/<int:id>', careers_views.careers_detail),
    path('home/',home_views.home_list),
    path('home/<int:id>',home_views.home_detail),
    path('hblogs/',home_views.hblogs_list),
    path('hblogs/<int:id>',home_views.hblogs_detail),
    path('awards/',awards_views.image),
    path('awards/<int:image_id>',awards_views.image),
    path('awards/',awards_views.awards_list),
    path('awards/<int:id>',awards_views.awards_detail)
]

#urlpatterns = format_suffix_patterns(urlpatterns)
######################
# 
# remove detailed error
# put standard error page after completion of website 
# remove detail pages
urlpatterns += static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)