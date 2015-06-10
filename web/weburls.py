#!/usr/bin/env python
# _*_coding:utf-8_*_
__author__ = 'zhuruiqing'
from django.conf.urls import patterns, include, url
from django.contrib import admin
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'day15.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/', views.login),
    url(r'^index/', views.index),
    #url(r'^index/(?P<page>\d*)', views.index),

)