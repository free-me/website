from django.shortcuts import render


def display(request):
    context = {}
    context['name'] = '小猪佩奇'
    return render(request, 'WWW/index.html',context)