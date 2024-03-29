"""ProperNounIndexSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import os

from django.conf.urls import url, include
from django.contrib import admin
from django.urls import re_path
from django.views.static import serve

from ProperNounIndexSystem import settings
from ProperNounIndexSystem.activator import process

admin.autodiscover()

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    # url(r'^admin/', include('django.contrib.admin.urls')),

    url(r"^Main/index/(\w*)", include("Main.urls")),
    url(r'^(?P<app>(\w+))/(?P<function>(\w+))/(?P<page>(\w+))/(?P<id>(\w+))/$', process),
    url(r'^(?P<app>(\w+))/(?P<function>(\w+))/(?P<id>(\w+))/$', process),
    url(r'^(?P<app>(\w+))/(?P<function>(\w+))/$', process),
    url(r'^(?P<app>(\w+))/$', process, {'function': 'index'}),
    re_path(r'^image/(?P<path>.*)$', serve, {'document_root': os.path.join(settings.BASE_DIR, 'image')}),

]

