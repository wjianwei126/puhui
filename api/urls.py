from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
import api
import views

router = routers.DefaultRouter()
router.register(r'user', api.UserViewSet)
#router.register(r'group', views.GroupViewSet)
router.register(r'view_asset', api.AssetViewSet)
router.register(r'cmdb_user', api.UserProfileViewSet)
router.register(r'business_unit', api.BusinessUnitViewSet)
router.register(r'business_unit_level2', api.BusinessUnitLevel2ViewSet)
router.register(r'status', api.StatusViewSet)
router.register(r'manufactory', api.ManufactoryViewSet)
router.register(r'product_version', api.ProductVersionViewSet)
router.register(r'contract', api.ContractViewSet)
router.register(r'idc', api.IDCViewSet)
router.register(r'server', api.ServerViewSet)
router.register(r'network_device', api.NetworkDeviceViewSet)
router.register(r'software', api.SoftwareViewSet)
router.register(r'cpu', api.CPUViewSet)
router.register(r'monitor', api.MonitorViewSet)
router.register(r'nic', api.NICViewSet)
router.register(r'disk', api.DiskViewSet)
router.register(r'tag', api.TagViewSet)
router.register(r'memory', api.MemoryViewSet)
router.register(r'maintainence', api.MaintainenceViewSet)
router.register(r'raid_adaptor', api.RaidAdaptorViewSet)
router.register(r'asset_status', api.AssetStatusViewSet)
router.register(r'os_installation', api.OSInstallViewSet)
router.register(r'raid_configuration', api.RaidConfigViewSet)
router.register(r'partition_configuration', api.PartitionConfigViewSet)
router.register(r'nic_configuration', api.NICConfigViewSet)


urlpatterns = patterns('',    
    url(r'^', include(router.urls)),
    url(r'submit', views.submit),
    url(r'auth',views.checkUser),
    url(r'show',views.show),

    #url(r'index/', views.index),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
