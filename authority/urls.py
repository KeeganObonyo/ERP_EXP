from django.conf.urls import url
from authority.views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^get_permissions/$', PermissionListAPIView.as_view(),
        name='permission_list'),
    url(r'^add_permissions/$', PermissionAddAPIView.as_view(),
        name='permission_list'),
    url(r'^permission/(?P<pk>\d+)/$', PermissionDetailAPIView.as_view(),
        name='thread'),
]
