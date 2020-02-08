from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    '''
        文章分类
    '''
    name = models.CharField("分类", max_length=100)

    class Meta:
        verbose_name="分类"
        verbose_name_plural="分类"

    def __str__(self):
        return self.name



class Tag(models.Model):
    '''
       标签
    '''
    name = models.CharField("标签", max_length=100)

    class Meta:
        verbose_name="标签"
        verbose_name_plural="标签"

    def __str__(self):
        return self.name


class Post(models.Model):
    '''
       文章
    '''
    class Meta:
        verbose_name="文章"
        verbose_name_plural="文章"


    title = models.CharField("标题", max_length=100)
    body = models.TextField("文章内容")
    created_time = models.DateTimeField("创建时间", default=timezone.now)
    modified_time = models.DateTimeField("修改时间")
    # 文章摘要
    excerpt = models.CharField("摘要", max_length=200, blank=True)
    # 外链接类别， 一对多
    category = models.ForeignKey(Category, verbose_name="类别",on_delete=models.CASCADE)
    # 与标签多对多
    tags = models.ManyToManyField(Tag, verbose_name="标签",blank=True)
    # 和作者一对多
    author = models.ForeignKey(User, verbose_name="作者", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):  # model有个save方法， 在外部调用save时触发
        self.modified_time = timezone.now()  # 多增加了功能
        super().save(*args, **kwargs)  
    
    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"pk":self.pk})

    def __str__(self):
        return self.title




