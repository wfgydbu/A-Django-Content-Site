from django.conf.urls import url

from . import views

app_name = 'sticker'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('about/', views.about, name='about'),
    url(r'^sticker/(?P<md5>[0-9a-z]+)/$', views.singleDetailView.as_view(), name='single'),
    url(r'^category/(?P<cate>.*?)/$', views.categoryListView.as_view(), name='category'),
]