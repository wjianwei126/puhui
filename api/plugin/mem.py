#!/usr/bin/env python
# _*_coding:utf-8_*_
__author__ = 'zhuruiqing'
from api import models
import time

def mem(ass_data):
    asset_id = ass_data['asset_id']

    mem_dic = {
        'sn':ass_data.get('sn'),
        'manufactory':ass_data.get('manufactory'),
        'ram':ass_data.get('ram')
        }
    ram_dic = mem_dic['ram']
    oldmem = None
    oldmem = models.Memory.objects.filter(parent_sn=asset_id)


    if oldmem :
        for k1,v1 in ram_dic.items():  #k1 slot号，v1 字典包括model  capacity等等
            for i in oldmem: #遍历查询出的对象的列表
                if i.__dict__.get('slot') == k1:  #对列表的每个值的slot比较
                    for k2,v2 in v1.items():  #遍历 每个slot 字典
                        if v2 == i.__dict__.get(k2): #比较字典内的每一项
                            pass
                        else:
                            currentTime = time.strftime("%Y-%m-%d %H:%M:%S")
                            logDetail = u"%s由[%s]变更为[%s]"%(k2,i.__dict__.get(k2),v2,)
                            models.Maintainence.objects.create(name='资产变更',
                                    maintain_type=1,
                                    description=logDetail,
                                    device_sn=asset_id,
                                    memo='ceshi',
                                    event_start=currentTime,
                                    event_end=currentTime,
                                    applicant=models.UserProfile.objects.get(id=1),
                                    performer=models.UserProfile.objects.get(id=1))
                    models.Memory.objects.filter(slot=k1).update(**v1)

                else:
                    continue
    else:
        try:

            for k,v in ram_dic.items():
                models.Memory.objects.create(sn=v.get('sn'),
                      parent_sn=asset_id,
                      slot=k,
                      manufactory=v.get('manufactory'),
                      model = v.get('model'),
                      capacity = v.get('capacity'))
        except Exception,e:
            print e