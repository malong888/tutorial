#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-3-21 下午8:16
# @Author  : Michael
# @Site    : 
# @File    : serializers.py.py
# @Software: PyCharm

# 创建一个序列化类
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

# 重写我们现有的序列化程序以使用超链接
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url','id','highlight','owner',
                  'title','code','linenos','language','style')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')

















# 第一部分定义了序列化/反序列化的字段
# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

# class SnippetSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')
#     class Meta:
#         model = Snippet
#         fields = ('id', 'title', 'code', 'linenos', 'language', 'style')
#
#     # create()和update()方法定义了在调用serializer.save()时如何创建和修改完整的实例
#     def create(self, validated_data):
#         """
#         根据提供的验证过的数据创建并返回一个新的`Snippet`实例。
#         """
#         return Snippet.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         根据提供的验证过的数据更新和返回一个已经存在的`Snippet`实例。
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance
#
# # 创建新的用户序列化
# class UserSerializer(serializers.ModelSerializer):
#     snippets = serializers.PrimaryKeyRelatedField(many=True,queryset=Snippet.objects.all())
#
#     class Meta:
#         model = User
#         fields = ('id','username','snippets')
#
