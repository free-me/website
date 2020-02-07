from django.shortcuts import render
from django.test import TestCase

# Create your tests here.
def index(request):
    context = {}
    context['test'] = "this is test msg!!!"
    return render(request,'article/1.html',context)