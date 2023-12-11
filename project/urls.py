from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from core.views import answer, index, trigger

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("trigger/", trigger),
    path("answer/", answer, name="answer"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
