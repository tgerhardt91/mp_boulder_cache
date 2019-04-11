
from django.urls import path, include
from django.contrib import admin
import hello.views

admin.autodiscover()


urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("managecache/", hello.views.managecache, name="managecache"),
    path("admin/", admin.site.urls),
]
