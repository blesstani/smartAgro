
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('intranet.urls')),
    path('', views.smartagro,name='smartagro'),
   
    
]
urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)