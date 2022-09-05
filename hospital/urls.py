from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  

urlpatterns = [
    path('admin/', admin.site.urls),

    # User management
    path('accounts/', include('allauth.urls')), 

    # local apps
    path('', include('main.urls')),
    path('referral/', include('referral.urls')),
    path('recipe/', include('recipe.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)