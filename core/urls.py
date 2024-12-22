from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from core import settings
from landing.views import landing, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing, name='index'),
    path('contact/', contact, name='contact')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
