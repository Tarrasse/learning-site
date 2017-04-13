from . import views
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.course_list, name='course_list'),
    url(r'^(?P<course_pk>[0-9]+)/(?P<step_pk>[0-9]+)/$', views.step_detail, name='course_step'),
    url(r'^(?P<pk>[0-9]+)/$', views.course_detail, name='course_detail'),
]
