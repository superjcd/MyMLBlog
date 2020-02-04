from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
 
def index(request):
    return render(request, "blog/index.html", context={
        "title":'我的博客',
        "welcome":'欢迎阅读',
    })
    #return HttpResponse("欢迎访问我的博客首页！")
