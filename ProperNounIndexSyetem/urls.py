"""ProperNounIndexSyetem URL Configuration

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

from django.conf.urls import url

from ProperNounIndexSyetem.activator import process

urlpatterns = [

   # url(r"Main/", include("Main.urls")),
   # url(r"Admin/", include("Admin.urls")),

   url(r'^(?P<app>(\w+))/(?P<function>(\w+))/(?P<page>(\w+))/(?P<id>(\w+))/$', process),
   url(r'^(?P<app>(\w+))/(?P<function>(\w+))/(?P<id>(\w+))/$', process),
   url(r'^(?P<app>(\w+))/(?P<function>(\w+))/$', process),
   url(r'^(?P<app>(\w+))/$', process, {'function': 'index'}),

]
