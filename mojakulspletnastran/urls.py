from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mojakulspletnastran.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r"prva.html",'blog.views.prva_stran'),
    url(r'^admin/', include(admin.site.urls)),
    url(r"talepsa.html",'blog.views.talepsa'),
    
]
