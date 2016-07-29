"""kudobuzzAsker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import patterns, include, url
from django.contrib import admin
from kudobuzzAsker import settings

urlpatterns = [
	url(r'^$', 'asker.views.index', name='home'),
	url(r'^basic-shopify/$', 'asker.views.basic_shopify', name='basic_shopify'),
	url(r'^basic-shopify/(?P<question_id>[0-9]+)/$', 'asker.views.next_question', name='next_question'),
	url(r'^asker/', include('asker.urls')),
    url(r'^admin/', admin.site.urls),
]

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
