#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-3-21 下午8:59
# @Author  : Michael
# @Site    : 
# @File    : urls.py
# @Software: PyCharm

# 我们需要把这些视图连起来。创建一个snippets/urls.py文件


from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from snippets import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^', include(router.urls))
]



# from django.conf.urls import url,include
# from rest_framework.urlpatterns import format_suffix_patterns
# from snippets import views
#
# # 将ViewSet类绑定到一组具体视图中
# from snippets.views import SnippetViewSet, UserViewSet, api_root
# from rest_framework import renderers
# # from rest_framework.schemas import get_schema_view
#
# # schema_view = get_schema_view(title='Pastebin API')
#
# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })
# # 在URL conf中注册视图
# urlpatterns = format_suffix_patterns([
#     url(r'^$', api_root),
#     url(r'^snippets/$', snippet_list, name='snippet-list'),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail, name='snippet-detail'),
#     url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name='snippet-highlight'),
#     url(r'^users/$', user_list, name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
#     # url('^schema/$', schema_view),
# ])









# 所有这些名称添加到我们的URLconf中后API端点

# urlpatterns = format_suffix_patterns([
# 	url(r'^$',views.api_root),
# 	url(r'^snippets/$',
# 		views.SnippetList.as_view(),
# 		name='snippet-list'),
# 	url(r'^snippets/(?P<pk>[0-9]+)/$',
# 		views.SnippetDetail.as_view(),
# 		name='snippet-detail'),
# 	url(r'snippets/(?P<pk>[0-9]+)/highlight/$',
# 		views.SnippetHighlight.as_view(),
# 		name='snippet-highlight'),
# 	url(r'^users/$',
# 		views.UserList.as_view(),
# 		name='user-list'),
# 	url(r'^users/(?P<pk>[0-9]+)/$',
# 		views.UserDetail.as_view(),
# 		name='user-detail')
# ])
# # 可浏览API的登录和注销视图
# urlpatterns += [
#     url(r'^api-auth/', include('rest_framework.urls',
#                                namespace='rest_framework')),
# ]



# urlpatterns = [
# 	url(r'^snippets/$',views.SnippetList.as_view()),
# 	url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
# 	url(r'^users/$',views.UserList.as_view()),
# 	url(r'users/(?P<pk>[0-9]+)/$',views.UserDetail.as_view()),
# 	url(r'^$',views.api_root),
# 	url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view()),
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)