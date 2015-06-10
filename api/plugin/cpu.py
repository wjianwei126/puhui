#!/usr/bin/env python
# _*_coding:utf-8_*_
__author__ = 'zhuruiqing'
from api import models
import time

def cpu(ass_data):
    asset_id = ass_data['asset_id']

    cpu_dic = {
        'sn':ass_data.get('sn'),
        'model':ass_data.get('cpu_model'),
        'manufactory':ass_data.get('manufactory'),
        }
    oldCpu = None
    oldCpu = models.CPU.objects.filter(parent_sn=asset_id)
    if oldCpu :
        oldCpu_dic = oldCpu[0].__dict__
        for k,v in cpu_dic.items():
            if v == oldCpu_dic[k]:
                pass
            else:

                currentTime = time.strftime("%Y-%m-%d %H:%M:%S")
                logDetail = u"%s由[%s]变更为[%s]"%(k,oldCpu_dic[k],v,)
                #print logDetail
                models.Maintainence.objects.create(name='资产变更',
                                                    maintain_type=1,
                                                    description=logDetail,
                                                    device_sn=asset_id,
                                                    memo='ceshi',
                                                    event_start=currentTime,
                                                    event_end=currentTime,
                                                    applicant=models.UserProfile.objects.get(id=1),
                                                    performer=models.UserProfile.objects.get(id=1))
        models.CPU.objects.filter(parent_sn=asset_id).update(**cpu_dic)
    else:
        try:
            models.CPU.objects.create(sn=cpu_dic['sn'],
                                      parent_sn=asset_id,
                                      model=cpu_dic['model'],
                                      manufactory=cpu_dic['manufactory'])
        except Exception,e:
            print e