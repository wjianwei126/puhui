#!/usr/bin/env python
#coding:utf-8
from rest_framework import viewsets
from models import *
from serializers import *

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


    
class AssetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Asset.objects.all()
    #serializer_class = AssetSerializer2
    serializer_class = AssetSerializer
    
    '''
    def get_queryset(self):
        print '=====goes herer....'
        return self.queryset
    #@list_route()
    def get_asset(self, request): 
        qu = Asset.objects.all()

       
        serializer = AssetSerializer(data=qu)
        return Response(serializer.data)
    @list_route()
    def detail(self,request):
        device_type = request.GET.get('device_type')
        asset_id = request.GET.get('asset_id')
        device_obj = divice_types_dic.get(device_type)
        print 'line539:',device_type
        if device_obj is not None:
            try:
                table_obj,serializer_class = device_obj 
                table_data = table_obj.objects.get(asset_id=asset_id)
                #print 'line 380..',table_data
                #serializer_class.Meta.depth = 2
                #table_data.alex='test'
                serializer_obj = serializer_class(table_data, context={'request': request})
                print 'here...line548' #,serializer_obj.data
                return Response(serializer_obj.data)
                #return HttpResponse('jj')
            except ObjectDoesNotExist,e:
                return ResponseData(data='',message=str(e))
        else:
            return ResponseData(data='',message="invalid device_type '%s' " % device_type)        
    '''    
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
class BusinessUnitViewSet(viewsets.ModelViewSet):
    queryset = BusinessUnit.objects.all()
    serializer_class = BusinessUnitSerializer 
class BusinessUnitLevel2ViewSet(viewsets.ModelViewSet):
    queryset = BusinessUnitLevel2.objects.all()
    serializer_class = BusinessUnitLevel2Serializer    
class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer    

class ManufactoryViewSet(viewsets.ModelViewSet):
    queryset = Manufactory.objects.all()
    serializer_class = ManufactorySerializer    
class ProductVersionViewSet(viewsets.ModelViewSet):
    queryset =  ProductVersion.objects.all()
    serializer_class = ProductVersionSerializer   
class ContractViewSet(viewsets.ModelViewSet):
    queryset =  Contract.objects.all()
    serializer_class = ContractSerializer   
class IDCViewSet(viewsets.ModelViewSet):
    queryset =  IDC.objects.all()
    serializer_class = IDCSerializer   
class ServerViewSet(viewsets.ModelViewSet):
    queryset =  Server.objects.all()
    serializer_class = ServerSerializer   
class NetworkDeviceViewSet(viewsets.ModelViewSet):
    queryset =  NetworkDevice.objects.all()
    serializer_class = NetworkDeviceSerializer   
class SoftwareViewSet(viewsets.ModelViewSet):
    queryset =  Software.objects.all()
    serializer_class = SoftwareSerializer   
class CPUViewSet(viewsets.ModelViewSet):
    queryset =  CPU.objects.all()
    serializer_class = CPUSerializer   
class MonitorViewSet(viewsets.ModelViewSet):
    queryset =  Monitor.objects.all()
    serializer_class = MonitorSerializer   
class DiskViewSet(viewsets.ModelViewSet):
    queryset =  Disk.objects.all()
    serializer_class = DiskSerializer   
class NICViewSet(viewsets.ModelViewSet):
    queryset =  NIC.objects.all()
    serializer_class = NICSerializer 
class MaintainenceViewSet(viewsets.ModelViewSet):
    queryset =  Maintainence.objects.all()
    serializer_class = MaintainenceSerializer   

class MemoryViewSet(viewsets.ModelViewSet):
    queryset =  Memory.objects.all()
    serializer_class = MemorySerializer   
class RaidAdaptorViewSet(viewsets.ModelViewSet):
    queryset =  RaidAdaptor.objects.all()
    serializer_class = RaidAdaptorSerializer  
class AssetStatusViewSet(viewsets.ModelViewSet):
    queryset =  AssetStatus.objects.all()
    serializer_class = AssetStatusSerializer  

class OSInstallViewSet(viewsets.ModelViewSet):
    queryset = Configuration.objects.all()
    serializer_class = OSInstallSerializer
class RaidConfigViewSet(viewsets.ModelViewSet):
    queryset = RaidConfig.objects.all()
    serializer_class = RaidConfigSerializer    
    
class PartitionConfigViewSet(viewsets.ModelViewSet):
    queryset = PartitionConfig.objects.all()
    serializer_class = PartitionConfigSerializer     
class NICConfigViewSet(viewsets.ModelViewSet):
    queryset = NICConfig.objects.all()
    serializer_class = NICConfigSerializer      
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer      
    


