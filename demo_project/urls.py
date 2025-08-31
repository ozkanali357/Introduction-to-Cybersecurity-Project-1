from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse  # Add this import

urlpatterns = [
    path('', lambda request: HttpResponse("Welcome to the Django OWASP Demo!"), name='home'),  # Add this line
    path('admin/', admin.site.urls),
    path('vulnerabilities/', include('vulnerabilities.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)