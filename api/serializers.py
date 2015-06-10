#!/usr/bin/env python
#coding:utf-8

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'email')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        #fields = ('url', 'name')
        
class AssetSerializer(serializers.HyperlinkedModelSerializer):
    #sn = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Asset
class ServerSerializerForOSInstall(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Server
        fields = ('manufactory','sn')
        #depth = 1        
class AssetSerializerForOSInstall(serializers.HyperlinkedModelSerializer):
    server = ServerSerializerForOSInstall(read_only=True )
    class Meta:
        model = Asset
        fields = ('id','hostname','server')
        depth = 1
      
class OSInstallSerializer(serializers.ModelSerializer):   
    #server_info = serializers.SerializerMethodField('get_server_info') 
    asset = AssetSerializerForOSInstall(read_only=True )
     
    class Meta:
        model = Configuration     
        depth = 2
        fields = ('id','asset','defined_raid_types','defined_partitions',
                  'management_ip','business_ip','business_netmask','business_gateway', 
                  'vlan_id','os','os_install_zone')
   
    def get_server_info(self,obj):   
        asset_id = obj.asset_id
        config_obj = Server.objects.filter(asset_id=asset_id)[0]
        #print 'get_configuration:', config_obj
        data_dic = {'manufactory': config_obj.manufactory}
        return data_dic      
class ConfigurationSerializer(serializers.ModelSerializer):       
    class Meta:
        model = Configuration     
        #depth = 1
        fields = ('id','management_ip','business_ip')
          
class AssetStatusSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = AssetStatus

class AssetSerializer2(serializers.HyperlinkedModelSerializer):
    #id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #print '---here---'
    assetstatus = AssetStatusSerializer()
    
    class Meta:
        model = Asset
        depth = 2
        fields = ('id','device_type','name','hostname','server','asset_op','contract',
                  'trade_time' ,'expire_time','tag',
                  'warranty','price','business_unit','admin', 'idc',
            'cabinet_num',
            #'configuration__management_ip',
            'cabinet_order' ,
            'memo',
            'assetstatus',
            'create_at',
            'update_at')
        
        
class BusinessUnitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BusinessUnit
        '''fields = (
            'url',
           'name', 
        )'''
class BusinessUnitLevel2Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BusinessUnitLevel2
class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status        
class ManufactorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manufactory
class ProductVersionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductVersion
class ContractSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contract
class IDCSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IDC
            
class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    #user = UserSerializer()
    #backup_name = UserSerializer()
    #leader = UserSerializer()
    #business_unit = BusinessUnitSerializer()
    class Meta:
        model = UserProfile
class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        #depth=3
        print '99:server detail'
        model = Server
        #
class ServerDetailSerializer(serializers.ModelSerializer):
    configs = serializers.SerializerMethodField('get_configuration')
    class Meta:
        model = Server 
        #print 'serializers 103:'
        depth = 3
        fields = ('id','sn','created_by','manufactory','asset', 'configs',
                  'model','cpu_count','cpu_count','cpu_core_count','cpu_model','nic',
                  'raid_type','physical_disk_driver','raid_adaptor','ram_size','ram',
                  'os_type','os_distribution','os_release','create_at','update_at')

    def get_configuration(self,obj):   
        asset_id = obj.asset_id
        config_obj = Configuration.objects.filter(asset_id=asset_id)[0]
        #print 'get_configuration:', config_obj
        data_dic = {'management_ip': config_obj.management_ip,
                    'business_ip': config_obj.business_ip}
        return data_dic

class ServerSerializer2(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Server 
        #depth = 2
class NetworkDeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NetworkDevice 
class SoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Software 
class DiskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Disk 
class CPUSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CPU 
class MonitorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Monitor 
class NICSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NIC 
        fields= ('id',
                 'name',
                 'netmask',
                 'parent_sn',
                 'sn',
                 'update_at',
                 'create_at',
                 'ipaddr',
                 'mac',
                 'manufactory',
                 'memo',
                 'model',
                 )     
class RaidAdaptorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RaidAdaptor 
class MemorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Memory 
class MaintainenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Maintainence 

class RaidConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = RaidConfig 
class PartitionConfigSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PartitionConfig 
     

class TaskLogSerializer(serializers.ModelSerializer):
    asset = AssetSerializerForOSInstall(read_only=True )
    class Meta:
        model = TaskLog
        #depth = 1
        fields = ('id','task','progress','result','log','asset','update_time')
class TaskCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskCenter
         
class NICConfigSerializer(serializers.HyperlinkedModelSerializer):     
    class Meta:
        model = NICConfig  
class TagSerializer(serializers.ModelSerializer):     
    class Meta:
        model = Tag       