
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("senior/", include("senior.urls")), # include는 기본 /senior/ 이라는 폴더에서 기본 default값으로 시작할거라는 것을 의미
]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

