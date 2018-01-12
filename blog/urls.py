from django.conf.urls import url
from django.views.generic import DetailView
from blog.models import Post
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Post, template_name='blog/post.html')),
]