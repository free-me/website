import datetime
from django.http import HttpResponse
from django.views.generic import View

class jump404(View):
    def get(self,request):
        d='99.9'
        try:
            offset = int(d)
        except ValueError:
            raise self.Http404()
        dt = datetime.datetime.now()+datetime.timedelta(hours=d)
        html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (str(d), dt)
        return HttpResponse(html)
    def Http404(self):
        return HttpResponse("404测试函数！！！")