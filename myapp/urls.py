from django.conf.urls import patterns, url

from myapp import views


urlpatterns = patterns('',
    url(r'home', views.home,
        name='home',),
    url(r'login', views.login_user,
        name='login_user',),
    url(r'register', views.register_user,
        name='register_user',),
)
