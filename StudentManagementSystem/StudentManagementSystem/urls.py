from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import Views,HODViews,StudentViews,StaffViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',Views.BASE,name='base'),
    #login path
    path('login/',Views.LOGIN,name='login'),

    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
