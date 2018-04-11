"""guideForBeauty URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView


import beauty
from beauty import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^beauty/', include("beauty.url"), ),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^focus/$', TemplateView.as_view(template_name="index.html")),

    # 这个页面的路由是前端页面路由
    # 后台接口路由请放到beauty下的url.py中
]
