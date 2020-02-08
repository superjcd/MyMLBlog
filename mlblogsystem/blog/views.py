from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.
 
def index(request):
    post_list = Post.objects.all().order_by("-created_time")  # 倒序排列
    return render(request, "blog/index.html", context={
        "post_list":post_list})


def detail(request, pk):  # pk是url传入的
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/detail.html", context={
        "post":post
    })
    
