from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Category
import markdown

# Create your views here.
 
''' 
   数据经过：DB - VIEW - 前段的一整套流程， 意味着VIEW可以修改数据内容及格式再呈现给前段

'''

def index(request):
    post_list = Post.objects.all().order_by("-created_time")  # 倒序排列
    return render(request, "blog/index.html", context={
        "post_list":post_list})


def archive(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month).order_by("-created_time")
    return render(request, )


def detail(request, pk):  # pk是url传入的
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body, 
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, "blog/detail.html", context={
        "post":post
    })
    

def category(request, pk):
    # 首先获取的是类别
    cat = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cat).order_by("-created_time")
    return render(request, "blog/index.html", context={
        "post_list":post_list
    })


def tag(request, pk):
    # 记得在开始部分导入 Tag 类
    t = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=t).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

