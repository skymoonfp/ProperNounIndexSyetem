#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     urls
 IDE：    PyCharm
创建时间： 2019/6/3 17:08
@author： skymoon
"""

from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from Main.views import *


# ============= User开始 =============
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# ============= User结束 =============


# ============= UserInfo开始 =============
class UserInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserInfo
        fields = (
        'id', 'username', 'password', 'birthday', 'e_mail', 'mobile', 'identify_code', 'create_time', 'user_class')


class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer


# ============= UserInfo结束 =============


# ============= UserClass开始 =============
class UserClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserClass
        fields = ('id', 'user_class_name')


class UserClassViewSet(viewsets.ModelViewSet):
    queryset = UserClass.objects.all()
    serializer_class = UserClassSerializer


# ============= UserClass结束 =============


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'UserInfo', UserInfoViewSet)
router.register(r'UserClass', UserClassViewSet)


urlpatterns = [

    url(r'^', include(router.urls)),

]
