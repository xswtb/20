from django.shortcuts import render,HttpResponse
from django.views import View
# Create your views here.
def index(request):
    return HttpResponse("Index")

class IndexView(View):
    def dispatch(self, request, *args, **kwargs):
        print('before')
        res = super(IndexView,self).dispatch(request,*args,**kwargs)
        print('after')
        return res
    def get(self,request,*args,**kwargs):

        return render(request,"index.html")
    def post(self,request,*args,**kwargs):
        return HttpResponse("999")