from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from .userDataModels import userData

#搜索初始页面
class searchIndex(View):
    def get(self,requests):
        # print('==================')
        return render(requests,'article/f.html')

#搜索执行页面
class searchForm(View):
    def get(self,requests):
        requests.encoding='utf-8'
        print('=====')
        if 'q' in requests.GET:
            try:
                result = userData.objects.filter(userName=requests.GET['q']).first()
                msg = '数据库内容：'+str(result.userId)+result.userName+result.phone+result.passWord
            except AttributeError:
                msg='未查询到任何信息！！'
        else:
            msg = '内容不能为空'
        # message='111111111'
        return HttpResponse(msg)