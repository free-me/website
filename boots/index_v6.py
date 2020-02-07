from django.shortcuts import render


def display6(request):
    context = {}
    return render(request,'www/index_v6.html')