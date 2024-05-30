from django.urls import path
from django.contrib import admin
from . import views
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include


urlpatterns = []
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
