from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render

from .models import StudentModel
from .models import HostList
from django.views.generic import View
#数据添加
class addhosts(View):
    def get(self,requests):
        hosts =[]
        ports =[]
        HostList.objects.create(host='127.0.0.2',port=8000,appName='django',url='localhost:8000/')
        result = HostList.objects.filter(host='127.0.0.2')
        print('=============')
        for ite in result:
            hosts.append(ite.host)
            ports.append(ite.port)
        context ={}
        context['hosts']=hosts
        context['ports']=ports
        for ite in result:
            print(ite.host)
            print(ite.port)
        print('=============')
        # return HttpResponse(result[0].host)
        return render(requests,'article/search.html',context)
#数据查询
class search(View):
    def get(self,requests):
        hosts =[]
        ports =[]
        result = HostList.objects.filter(host='127.0.0.2')
        print('=============')
        for ite in result:
            hosts.append(ite.host)
            ports.append(ite.port)
        context ={}
        context['hosts']=hosts
        context['ports']=ports
        # return HttpResponse(result[0].host)
        return render(requests,'article/search.html',context)
#数据修改
class modifyd(View):
    def get(self,response):
        result = HostList.objects.filter(host='127.0.0.1').update(appName='django学习')
        result = HostList.objects.filter(host='127.0.0.1')
        print('主机名:' + '\t\t' + '端口号：'  + '\t' + '应用名称:')
        print('===================================================')
        for ite in result:
            print('主机:'+ite.host+'\t'+'端口号：'+str(ite.port)+'\t'+'应用名称:'+ite.appName)
        return HttpResponse('修改成功')

#数据删除
class delData(View):
    def get(self,response):
        try:
            result = HostList.objects.filter(host='127.0.0.1').first().delete()
            msg='数据删除成功！！'
        except AttributeError:
            msg='已经没有数据'
        result = HostList.objects.filter(host='127.0.0.1')
        print('主机名:' + '\t\t' + '端口号：' + '\t' + '应用名称:')
        print('===================================================')
        for ite in result:
            print('主机:' + ite.host + '\t' + '端口号：' + str(ite.port) + '\t' + '应用名称:' + ite.appName)
        return HttpResponse(msg)