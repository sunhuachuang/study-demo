from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='articles_index'),
    url(r'^(?P<article_id>[0-9]+)/$', views.details, name='articles_details'),
]
