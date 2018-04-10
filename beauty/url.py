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
from django.conf.urls import url
from beauty import views
from beauty.lcj.handler import database_handler

urlpatterns = [
    url(r'show_student$', views.show_student, ),
    url(r'add_student$', views.show_student, ),
    url(r'show_baseMakeup$', views.show_baseMakeup, ),  # 这个估计可以删掉
    url(r'show_list$', views.show_list, ),
    url(r'show_search_list$', views.show_search_list, ),

    #  cj 接口路由
    url(r'^productsList/getProductsPage', database_handler.handle_search),
]
