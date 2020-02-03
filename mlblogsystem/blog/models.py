from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    '''
        文章分类
    '''
    name = models.CharField(max_length=100)



class Tag(models.Model):
    '''
       标签
    '''
    name = models.CharField(max_length=100)


class Post(models.Model):
    '''
       文章
    '''
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    # 文章摘要
    excerpt = models.CharField(max_length=200, blank=True)
    # 外链接类别， 一对多
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # 与标签多对多
    tags = models.ManyToManyField(Tag, blank=True)
    # 和作者一对多
    author = models.ForeignKey(User, on_delete=True)




