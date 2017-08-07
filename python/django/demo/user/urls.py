from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='users_index'),
    url(r'^(?P<pk>[0-9]+)/$', views.details, name='users_details'),
]
