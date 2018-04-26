from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
	url(r'^$',	views.signup, name='class'),
	url(r'^courses/$', views.course_list, name='course_list'),
	url(r'^services/$', views.services, name="services"),
	url(r'^courses/(?P<pk>\d+)/$',	views.course_read,	name='course_read'),
	url(r'^courses/enroll/(?P<pk>\d+)/$', views.enroll, name='enroll'),
]