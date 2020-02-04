from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
 
def index(request):
    post_list = Post.objects.all().order_by("-created_time")  # 倒序排列
    return render(request, "blog/index.html", context={
        "post_list":post_list})
    
