#!/usr/bin/env python
# _*_coding:utf-8_*_
__author__ = 'zhuruiqing'
from api import models
import time

def nic(ass_data):
    asset_id = ass_data['asset_id']
    nic_dic = ass_data.get('nic')
    for k1,v1 in nic_dic.items():
        result = models.NIC.objects.filter(parent_sn=asset_id,name=k1)
        f_dict = {
            'ipaddr':v1.get('ipaddress'),
            'mac':v1.get('macaddress'),
            'netmask':v1.get('netmask'),
            'model':v1.get('model'),
            }
        if result :
            result = result[0].__dict__
            print result,k1

            #print type(result),result
            print '%%%%%%%%'
            for k2,v2 in f_dict.items():
                print k2
                print v2
                print '*******************'
                print  result.get(k2)
                if v2 == result.get(k2):
                    pass
                else:
                    currentTime = time.strftime("%Y-%m-%d %H:%M:%S")
                    logDetail = u"%s由[%s]变更为[%s]"%(k2,result.get(k2),v2,)
                    models.Maintainence.objects.create(name='资产变更',
                        maintain_type=1,
                        description=logDetail,
                        device_sn=asset_id,
                        memo='ceshi',
                        event_start=currentTime,
                        event_end=currentTime,
                        applicant=models.UserProfile.objects.get(id=1),
                        performer=models.UserProfile.objects.get(id=1))
            models.NIC.objects.filter(parent_sn=asset_id,name=k1).update(**f_dict)
        else:

            models.NIC.objects.create(parent_sn=asset_id,
                                  name = k1,
                                  model = v1.get('model'),
                                  ipaddr = v1.get('ipaddress'),
                                  mac = v1.get('macaddress'),
                                  netmask = v1.get('netmask')
                                  )


