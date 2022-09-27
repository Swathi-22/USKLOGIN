from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('web.urls',namespace="web")),

    path('tinymce/', include('tinymce.urls')),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "USKLOGIN.COM Administration"
admin.site.site_title = "USKLOGIN.COM Admin Portal"
admin.site.index_title = "Welcome to USKLOGIN.COM Admin Portal"

