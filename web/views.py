#!/usr/bin/env python
# coding:utf-8
from django.shortcuts import render, render_to_response, redirect, HttpResponseRedirect, HttpResponse
from Helper import Checkcode
import StringIO
import urllib
import httplib
import json

# Create your views here.
def checkapi(source, params):  #向api发送用户名和密码进行验证
    headers = {"Content-type":"application/json"}
    host = '127.0.0.1'
    port = '8000'
    try:
        conn = httplib.HTTPConnection(host, port, 30) #实例化一个httplib类
        conn.request('POST',source,params,headers)
        response = conn.getresponse()
        original = response.read() #读取响应

    except Exception, e:
        print e

    return original

def login(request):
    if request.method == "POST":  # 获取htmlform表单内容
        data = {'username': request.POST.get('username'),
                'password': request.POST.get('password'),
                }
        data = json.dumps(data)
        source = '/api/auth/'
        result = checkapi(source, data)  # 发送验证信息
        request.session['is_login'] = 0
        if result == 'None':  # 判断api返回值
            return HttpResponseRedirect('/puhui/login/')
        else:
            request.session['user_name'] = request.POST.get('username')
            request.session['is_login'] = 1
            return HttpResponseRedirect('/puhui/index/')
    else:
        return render_to_response('login.html')
def judge_session(func):

        def wrapper(request): #传参  session验证
            try:
                print request.session['is_login']
                if request.session['is_login']:  #判断sessionid是否存在
                    return func(request)
                else:
                    return HttpResponseRedirect('/index/login/') #sessionid 不存在返回登录界面
            except Exception, e:
                print e
                return HttpResponseRedirect('/index/login/')

        return wrapper
@judge_session
def index(request):
    assertinfo = 'assertinfo'
    assertinfo = json.dumps(assertinfo)
    source = '/api/show/'
    result = checkapi(source,assertinfo)
    result = json.loads(result)
    print result,type(result)
    #return HttpResponse('welcome!!!!!!!!!!!')
    return render_to_response('index.html', {'data':result} )

