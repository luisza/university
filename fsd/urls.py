from django.urls import path
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'fsd.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    path('admin/',  admin.site.urls) ,
]
