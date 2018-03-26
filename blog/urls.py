from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post_content/(?P<post_id>[\d]+)/$', views.post_content, name='post_content'),
    url(r'^about$', views.about, name='about'),
    url(r'^comment/(?P<post_id>[\d]+)$', views.commet, name='comment'),
    url(r'^tags/(?P<tags_id>[\d]+)$', views.tag, name='tags'),
]
