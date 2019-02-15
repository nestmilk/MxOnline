# _*_ coding: utf-8 _*_
from users.views import UserinfoView

__author__ = 'nestmilk'
__date__ = '2019/2/15 15:19'

from django.conf.urls import url, include

urlpatterns = [
    #用户信息
    url(r'^info/$', UserinfoView.as_view(), name='user_info'),

]