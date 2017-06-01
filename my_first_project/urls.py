"""my_first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from hello.views import hello_world, single_greeting
from hello2.views import say_hello2
from hello.rest.login.login_viewset import Login
from register.rest.register.register_viewset import Register
from login_react.views import get_index
from hello.rest.greeting.greeting_viewset import GreetingViewset
from angular_todo.views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', hello_world),
    url(r'^api/greeting/$', GreetingViewset.as_view({'get': 'list', 'post': 'create'})),
    url(r'^api/greeting/(?P<pk>[0-9]+)/$', GreetingViewset.as_view({'get': 'retrieve', 'put': 'update', 'delete':'destroy'})),
    url(r'^hello/(?P<slug>[\w-]+)/$', single_greeting),
    url(r'^hello2/$', say_hello2),
    url(r'^login/$', Login.as_view()),
    url(r'register/$', Register.as_view()),
    url(r'todo/$', index),
    url(r'^$', get_index)
]
