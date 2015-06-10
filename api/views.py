#coding:utf-8
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse
from django.contrib.auth import authenticate,login
from rest_framework.decorators import api_view
from rest_framework.response import Response
from serializers import *
from plugin import cpu,mem,nic
import models
import json

@api_view(['GET', ])
def fetch_asset_id(request,hostname):
    #print 'line 418',hostname
    #print '==>',request.stream
    try:
        asset = Asset.objects.get(hostname__contains= hostname)
        data = {'asset_id': asset.id}
        return HttpResponse(json.dumps(data))
    except Exception,e:
        errors = [{'asset': e.message,'request_hostname': hostname }]
        return Response(data=errors, status=403,)


def ExecuteSubmit(ass_data,request):
    cpu.cpu(ass_data) #搜集cpu信息
    mem.mem(ass_data)
    nic.nic(ass_data)



@api_view(['POST','PUT','GET'])
def submit(request):
    ass_data = request.DATA
    #ass_data = json.loads(ass_data['data'])
    ass_data = ass_data['data']
    print ass_data
    ExecuteSubmit(ass_data,request)
    return Response('ok')


@api_view(['POST','GET'])
def checkUser(request):
    userinfo = request.DATA
    print userinfo
    user = authenticate(username=userinfo['username'],password=userinfo['password'])
    print type(user)

    if user is not None:
        return HttpResponse(user)

    else:
        return HttpResponse(None)


@api_view(['POST','GET'])
def show(request):
    assetinfo = request.DATA
    data = models.Asset.objects.filter().all()

    assetdata = {

    }
    for k,v in enumerate(data):
        print v,'&&&&&&&&&&',v.contract,type(v.contract)
        print type(k),type(v)
        assetdata[k] = [v.hostname, v.name, v.function]
    assetdata = json.dumps(assetdata)
    return HttpResponse(assetdata)

