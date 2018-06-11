# A-Django-Content-Site
这个项目是基于[Django 博客开发入门教程](http://zmrenwu.com/category/django-blog-tutorial/)的二次开发，你可以把它当成一个额外的练手项目，个人认为是Django的一个很不错的练手项目。

我的初衷是做一个内容展示平台，通过合理的结构和简单的开发就可以之前所做的爬虫的结果集展示出来。之后如果会继续做，就会朝着这个目标走。

关于本项目，还有一片技术博客：[使用Django框架开发一个网站](https://journal.ethanshub.com/post/category/gong-cheng-shi/-pythonkai-fa-djangokuang-jia-he-wang-zhan) 可供参考。

目前的网站看起来还是像个博客网站，因此比较适合展示面向文本的爬虫结果。当前网站默认带了从百度贴吧抓取的10个帖子，仅供测试使用。

## 使用

1. clone所有代码到本地。
2. 需要的Python有: `Django`和`markdown`。
3. 在项目根目录下运行：`python manage.py runserver 0.0.0.0:8000`。
4. 在浏览器中访问：`http://127.0.0.1:8000`。

也可以将其部署到其他地方，具体不表。