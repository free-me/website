from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def disp(request):
    msg = '这是一个测试页面！！！'
    return HttpResponse(msg)