from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sticker:category', kwargs={'cate': self.name})

class Sticker(models.Model):
    title  = models.CharField(max_length=70)
    author = models.CharField(max_length=70)

    content = models.TextField()
    md5 = models.CharField(max_length=32)

    created_time = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)

    # 贴吧名字
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title\

    def get_absolute_url(self):
        return reverse('sticker:single', kwargs={'md5': self.md5})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])