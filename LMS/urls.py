from django.conf.urls import url, include
from django.contrib.auth import views
from django.contrib import admin

urlpatterns = [
	url(r'^', include('lessons.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', views.login, name='login')
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
]
