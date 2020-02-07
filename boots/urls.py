from django.conf.urls import url
from . import views
from . import showMsg
from . import tests
from . import index_v6
from .mongoDisp import Student
from .manHostsL import *
from .seachApp import searApp
from .userManageView import *
from .djangoForm import *
from .E404ViewsModels import *
urlpatterns = [
    url(r'123/$',views.disp), #进行访问路由
    url(r'display/$', showMsg.display),
    url(r'test/$', tests.index),
    url(r'dis6/$',index_v6.display6),
    url(r'stu/$',Student.as_view(),name='stude'),
    url(r'addhost/$',addhosts.as_view(),name='add'),
    url(r'search/$',search.as_view(),name='search'),
    url(r'modify/$',modifyd.as_view(),name='modify'),
    url(r'delete/$',delData.as_view(),name='delete'),
    # url(r'searchindex/$',searApp.as_view(),name='searchindex')
    url(r'userAdd/$',userAddManage.as_view(),name='useradd'),
    url(r'userFind/$',userFindManage.as_view(),name='userfind'),
    url(r'userUpdate/$',userUpdateManage.as_view(),name='userUpdate'),
    url(r'userDelete/$',userDelManage.as_view(),name='userdel'),
    url(r'djangoSearch/$',searchIndex.as_view(),name='djangoSearch'),
    url(r'djangoSearchForm/$',searchForm.as_view(),name='djangoSearchForm'),
    url(r'showAdd/$',showUserAdd.as_view(),name='showuseradd'),
    url(r'jump404/$',jump404.as_view(),name='404'),

]

