
from django.contrib import admin
from django.urls import path, include
from China.views import *
from django.conf import settings
from django.conf.urls.static import static
from China.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index.html', Index),
    path('arogyasetu.html', ArogyaSetuApp)
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

