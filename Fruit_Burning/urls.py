"""Fruit_Burning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from  rest_framework.documentation import include_docs_urls

from .settings import MEDIA_ROOT
from django.views.static import serve
from user.views import UserViewset,UserListViewSet

from rest_framework_jwt.views import obtain_jwt_token
from user.views import LoginView,UserInfoView,app_login,app_register
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register(r'user',UserViewset,base_name="user")#用户注册接口

router.register(r'user-list',UserListViewSet,base_name="user-list")#用户列表

urlpatterns = [
    url('admin/', admin.site.urls),

    url(r'^app/reg/$',  app_register, name='app_register'),
    url(r'^app/login/$',  app_login, name='app_login'),

    #jwt的认证接口
    url(r'^user/login/$', LoginView.as_view(), name='login'),  # 用户的登陆url
    url(r'^user/info/', UserInfoView, name='user-info'),  # 用户的信息url
    url(r'^', include(router.urls)),

    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),#文件上传
    url(r'docs/',include_docs_urls(title="果蔬电商")),#接口文档
]
