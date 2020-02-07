from django.views.generic import View


def searApp(View):
    def searIndex(self,request):
        render(request,'article/search.html')
