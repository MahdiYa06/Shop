from django.contrib import admin
from filebrowser.sites import site as filebrowser_site
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/filebrowser/', filebrowser_site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('grappelli/', include('grappelli.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    path('admin/', admin.site.urls),
    
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
