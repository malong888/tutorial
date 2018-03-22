"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
# 使用路由器注册相应的视图集
from django.conf.urls import url, include
from snippets import views
from rest_framework.routers import DefaultRouter
#
# # 创建路由器并注册我们的视图
router = DefaultRouter()
router.register(r'snippets',views.SnippetViewSet)
router.register(r'users',views.UserViewSet)
#
# # API URL现在由路由器自动确定。
# # 另外，我们还要包含可浏览的API的登录URL。
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]



# from django.conf.urls import include, url
# from django.contrib import admin
#
# urlpatterns = [
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^',include('snippets.urls')),
# ]
# urlpatterns += [
#     url(r'^api-auth/', include('rest_framework.urls',
#                                namespace='rest_framework')),
# ]