from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'fsd.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    path('university/', include('university.urls')),
    path('admin/',  admin.site.urls) ,

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


