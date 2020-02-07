from django.http import HttpResponse
from .models import StudentModel
from .models import HostList
from django.views.generic import View


class Student(View):
    def get(self, request):
        #插入数据代码
        # StudentModel.objects.create(name='三月', age=18)
        # return HttpResponse('hello word!!!')

        # #修改数据代码
        # result = StudentModel.objects.filter(name='七月').first().update(name='8月')
        # print(result)

        #删除数据代码
        # result = StudentModel.objects.filter().first().delete()
        # print(result)
        HostList.objects.create(host='127.0.0.1',port=8000)
        return HttpResponse('测试数据')
    def post(self):
        result = StudentModel.objects.filter(name = '七月').first().update(name='8月')
        print(result)
        return HttpResponse('数据库内容为：'+result)