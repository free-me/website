from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import csrf

from .userDataModels import userData
from django.views.generic import View

class showUserAdd(View):
    def get(self,request):
        return render(request,'article/addUserPost.html')

class userAddManage(View):
    def get(self,request):
        if 'userName' in request.GET:
            userData.objects.create(userId=int(request.GET['userID']),userName=request.GET['userName'],passWord=request.GET['passWord'],phone=request.GET['phone'])
        return HttpResponse('数据插入成功！！')
    def post(self,request):
        ctx = {}#定义回传对象
        ctx.update(csrf(request))#
        print('=====')
        print(csrf(request).values())
        # print(request.POST['userName'])
        #print('===='+ctx.POST['userName']+'====')
        if request.POST:
            ctx['rlt']=request.POST['userName']#为回传对象赋值
        # print('=====post===='+request.POST['userName'])
        # return HttpResponse('数据提交成功')
        print(ctx)
        if 'userName' in request.POST:
            userData.objects.create(userId=int(request.POST['userID']),userName=request.POST['userName'],passWord=request.POST['passWord'],phone=request.POST['phone'])
            ctx['rlt'] = request.POST['userName']
        return render(request,'article/addUserPost.html',ctx)#进行回传

class userFindManage(View):
    def get(self,request):
        user = []
        result = userData.objects.filter()
        for ite in result:
            user.append(ite.userName)
            print(ite.userName)
        print('==========文件URL============')
        print(request.path)#输出请求url
        return HttpResponse(user)

class userUpdateManage(View):
    def get(self,request):
        result = userData.objects.filter(userName='三月').first().update(phone='18661834206')
        print('更新成功')
        return HttpResponse('更新成功')

class userDelManage(View):
    def get(self,request):
        userData.objects.filter(phone='18661834206').first().delete()
        print('删除成功')
        return HttpResponse('删除成功')