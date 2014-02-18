from __future__ import unicode_literals

from django.conf.urls import patterns, include, url

from django.contrib import admin

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_base.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',
        TemplateView.as_view(template_name='pages/home.html'),
        name="home"),
    #add the path to your new apps urls.py belo here, examples above.
    url(r'alamo-parkway/', include("AlamoParkway.urls", namespace="AlamoParkway")),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name="my_login"),
    url(r'^report_builder/', include('report_builder.urls')),
)
