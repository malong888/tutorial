from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from snippets.serializers import UserSerializer
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import detail_route

# 重构成视图集ViewSet

# 首先让我们将UserList和UserDetail视图重构为一个UserViewSet。我们可以删除这两个视图，并用一个类替换它们
class UserViewSet(viewsets.ReadOnlyModelViewSet):
	# 视图自动提供`list`和`detail`操作
	queryset = User.objects.all()
	serializer_class = UserSerializer

# 我们将替换SnippetList，SnippetDetail和SnippetHighlight视图类。我们可以删除三个视图，并再次用一个类替换它们
class SnippetViewSet(viewsets.ModelViewSet):
	"""
	此视图自动提供`list`，`create`，`retrieve`，`update`和`destroy`操作。

	另外我们还提供了一个额外的`highlight`操作。
	"""
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,
						  IsOwnerOrReadOnly,)

	# 我们还使用@detail_route装饰器创建一个名为highlight的自定义操作
	# 这个装饰器可用于添加不符合标准create/update/delete样式的任何自定义路径
	@detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
	def highlight(self,request,*args,**kwargs):
		snippet = self.get_object()
		return Response(snippet.highlighted)

	def perform_create(self,serializer):
		serializer.save(owner=self.request.user)


# @api_view装饰器创建一个API入口点
@api_view(['GET'])
def api_root(request,format=None):
	return Response({
		'users':reverse('user-list',request=request,format=format),
		'snippets':reverse('snippet-list',request=request,format=format)
	})






























# 用基类来表示实例创建高亮视图
# class SnippetHighlight(generics.GenericAPIView):
# 	queryset = Snippet.objects.all()
# 	renderer_classes = (renderers.StaticHTMLRenderer,)
#
# 	def get(self,request,*args,**kwargs):
# 		snippet = self.get_object()
# 		return Response(snippet.highlighted)
# REST框架提供了一组已经混合好（mixed-in）的通用视图，我们可以使用它来简化我们的views.py模块
# class SnippetList(generics.ListCreateAPIView):
# 	queryset = Snippet.objects.all()
# 	serializer_class = SnippetSerializer
# 	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
# 	# 序列化器的create()方法现在将被传递一个附加的'owner'字段以及来自请求的验证数据
# 	def perform_create(self, serializer):
# 		serializer.save(owner=self.request.user)
#
# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
# 	queryset = Snippet.objects.all()
# 	serializer_class = SnippetSerializer
# 	permission_classes = (permissions.IsAuthenticatedOrReadOnly,
# 						  IsOwnerOrReadOnly,)
#
#
# # 将用户展示为只读视图，因此我们将使用ListAPIView和RetrieveAPIView通用的基于类的视图
# class UserList(generics.ListAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer
#
# class UserDetail(generics.RetrieveAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer


















# # 通过使用mixin类编写视图
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
# from rest_framework import mixins
# from rest_framework import generics
#
#
# class SnippetList(mixins.ListModelMixin,
# 				  mixins.CreateModelMixin,
# 				  generics.GenericAPIView):
# 	queryset = Snippet.objects.all()
# 	serializer_class = SnippetSerializer
#
# 	def get(self, request, *args, **kwargs):
# 		return self.list(request, *args, **kwargs)
#
# 	def post(self, request, *args, **kwargs):
# 		return self.create(request, *args, **kwargs)
#
#
# class SnippetDetail(mixins.RetrieveModelMixin,
# 					mixins.UpdateModelMixin,
# 					mixins.DestroyModelMixin,
# 					generics.GenericAPIView):
# 	queryset = Snippet.objects.all()
# 	serializer_class = SnippetSerializer
#
# 	def get(self, request, *args, **kwargs):
# 		return self.retrieve(request, *args, **kwargs)
#
# 	def put(self, request, *args, **kwargs):
# 		return self.update(request, *args, **kwargs)
#
# 	def delete(self, request, *args, **kwargs):
# 		return self.destroy(request, *args, **kwargs)
#
#
#
#
# # 使用基于类的视图重写我们的API
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
#
# class SnippetList(APIView):
# 	# 列出所有的snippets或者创建一个新的snippet
# 	def get(self, request,format=None):
# 		snippets = Snippet.objects.all()
# 		serializer = SnippetSerializer(snippets,many=True)
# 		return Response(serializer.data)
#
# 	def post(self,request,format=None):
# 		serializer = SnippetSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class SinppetDetail(APIView):
# 	# 检索，更新或删除一个snippet示例
# 	def get_object(self,pk):
# 		try:
# 			return Snippet.objects.get(pk=pk)
# 		except Snippet.DoesNotExist:
# 			raise Http404
#
# 	def get(self,request,pk,format=None):
# 		snippet = self.get_object(pk)
# 		serializer = SnippetSerializer(snippet)
# 		return Response(serializer.data)
#
# 	def put(self,request,pk,format=None):
# 		snippet = self.get_object(pk)
# 		serializer = SnippetSerializer(snippet,data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# 	def delete(self,request,pk,format=None):
# 		snippet = self.get_object(pk)
# 		snippet.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)
#
#
#
# # 基于函数的视图
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
#
# @api_view(['GET','POST'])
# def snippet_list(request,format=None):
# 	# 列出所有的snippets，或者创建一个新的snippet
# 	if request.method == 'GET':
# 		snippets = Snippet.objects.all()
# 		serializer = SnippetSerializer(snippets,many=True)
# 		return Response(serializer.data)
#
# 	elif request.method == 'POST':
# 		serializer = SnippetSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET','PUT','DELETE'])
# def snippet_detail(request,pk,format=None):
# 	# 获取，更新或删除一个snippet实例
# 	try:
# 		snippet = Snippet.objects.get(pk=pk)
# 	except Snippet.DoesNotExist:
# 		return Response(status=status.HTTP_404_NOT_FOUND)
#
# 	if request.method == 'GET':
# 		serializer = SnippetSerializer(snippet)
# 		return Response(serializer.data)
#
# 	elif request.method == 'PUT':
# 		serializer = SnippetSerializer(snippet, data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# 	elif request.method == 'DELETE':
# 		snippet.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)
#
#
#
# from django.shortcuts import render
#
# # Create your views here.
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
#
# class JSONResponse(HttpResponse):
# 	# 将其内容呈现为JSON的HttpResponse
# 	def __init__(self,data,**kwargs):
# 		content = JSONRenderer().render(data)
# 		kwargs['content_type'] = 'application/json'
# 		super(JSONResponse, self).__init__(content, **kwargs)
#
# @csrf_exempt
# def snippet_list(request):
# 	# 列出所有的code snippet，或创建一个新的snippet
# 	if request.method == 'GET':
# 		snippets = Snippet.objects.all()
# 		serializer = SnippetSerializer(snippets,many=True)
# 		return JSONResponse(serializer.data)
# 	elif request.method == 'POST':
# 		data = JSONParser().parse(request)
# 		serializer = SnippetSerializer(data=data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return JSONResponse(serializer.data,status=201)
# 		return JSONResponse(serializer.errors,status=400)
#
# @csrf_exempt
# def snippet_detail(request,pk):
# 	# 获取，更新或删除一个 code snippet
# 	try:
# 		snippet = Snippet.objects.get(pk=pk)
# 	except Snippet.DoesNotExist:
# 		return HttpResponse(status=404)
#
# 	if request.method == 'GET':
# 		serializer = SnippetSerializer(snippet)
# 		return JSONResponse(serializer.data)
#
# 	elif request.method == 'PUT':
# 		data = JSONParser().parse(request)
# 		serializer = SnippetSerializer(snippet,data=data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return JSONResponse(serializer.data)
# 		return JSONResponse(serializer.errors,status=400)
#
# 	elif request.method == 'DELETE':
# 		snippet.delete()
# 		return HttpResponse(status=204)
#
