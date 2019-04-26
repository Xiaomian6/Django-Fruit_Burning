from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
import simplejson
import json
from rest_framework.views import APIView
from django.http import HttpResponse,JsonResponse
from rest_framework_jwt.utils import jwt_decode_handler
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
User = get_user_model()
from rest_framework.mixins import CreateModelMixin
from rest_framework import mixins
from rest_framework import viewsets
from .form import *
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.views.decorators.csrf import csrf_exempt
from .serializers import UserDetailSerializer,UserRegSerializer,UserSerializer
from django.contrib import auth


class  LoginView(APIView):
    def post(self,request,*args,**kwargs):
        tk = {}
        user_name = request.data.get("username")
        pass_word = request.data.get("password")
        try:
            user_info = User.objects.get(username=user_name,is_staff = True)
            if user_info.check_password(pass_word):
                if user_info is not None:
                    if user_info.is_active:
                        auth.login(request, user_info)
                        from rest_framework_jwt.settings import api_settings

                        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
                        payload = jwt_payload_handler(user_info)
                        token = jwt_encode_handler(payload)
                        res = {"code": 20000, "data": tk}
                        tk['token'] = token
                        # json = simplejson.dumps(dict, ensure_ascii=False)
                        return JsonResponse(res)
                    else:
                        data = {
                            "code": 60204,
                            "message": '账号已锁定',
                        }
                        return JsonResponse(data)
            data = {
                "code": 60204,
                "message": 'Account and password are incorrect.',
            }
            return JsonResponse(data)
        except Exception as e:
            data = {
                "code": 60204,
                "message": '账号不存在',
            }
            return JsonResponse(data)


@csrf_exempt
def UserInfoView(request):
    if request.method == 'GET':
        dict = {}
        # 获取请求参数token的值
        token=request.GET.get('token')
        user_info = None
        # 通过user_id查询用户信息
        try:
            # 顶一个空数组来接收token解析后的值
            toke_user = []
            toke_user = jwt_decode_handler(token)
            # 获得user_id
            user_id = toke_user["user_id"]
            user_info = User.objects.get(pk=user_id)
        except Exception as e:
            pass
        if user_info is not None:
            serializer = UserDetailSerializer(user_info, context={"request":request})
            user_data = serializer.data
            user_data['roles'] = 'admin'
            print(user_data)
            data = {

                "data": user_data,
                "code": 20000,
            }
            return JsonResponse(data)
        else:
            data = {
                "code": 20000,
                "message": "ALogin failed, unable to get user details."
            }
            return JsonResponse(data)





class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(user_name=username)|Q(user_phone=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

#注册视图
class UserViewset(CreateModelMixin,viewsets.GenericViewSet):
    """
    用户
    """
    serializer_class = UserRegSerializer
    queryset = User.objects.all()



#分页设置，如果在这里设置了分页，那么就不用在setting里面在设置分页了
from rest_framework.pagination import PageNumberPagination
class UserPagination(PageNumberPagination):
    page_size = 10  #也可以在url上设置每页多少个http://127.0.0.1:8000/goods/?p=2&page_size=20
    page_size_query_param = 'page_size'
    page_query_param = "p" #p代表第几页参数，及"http://127.0.0.1:8000/goods/?p=2",
    max_page_size = 100




#api最重要的view功能
from rest_framework import viewsets
#由于viewset没有继承mixin里面的get和post方法，所以得继承mixin的
#用了viewset方法，则url的设置方法不同其他的方法了

from django_filters.rest_framework import DjangoFilterBackend
class UserListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
        获取所有用户列表数据
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserPagination
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user_name','user_phone')

from .serializers import UserListSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class UserListView(APIView):
    def get(self, request, format=None):
        user = User.objects.all()[:10]
        user_serializer = UserListSerializer(user, many=True, context={"request":request})
        data = {
            "code": 20000,
            "data": user_serializer.data
        }
        return Response(data)



@csrf_exempt
def app_login(request):
    dict = {}
    try:
        if request.method == 'POST':
            req = simplejson.loads(request.body)
            username = req['username']
            password = req['password']
            print("request.body={}".format(request.body))
            try:
                user_info = User.objects.get(Q(user_name=username,is_staff = False) | Q(user_phone=username,is_staff = False))
                if user_info.check_password(password):
                    if user_info is not None:
                        if user_info.is_active:
                            auth.login(request, user_info)
                            return HttpResponse('200')
                return HttpResponse('201')
            except Exception as e:
                return HttpResponse('202')
    except Exception as info:
        print(info)
    if request.method == 'GET':
        return HttpResponse('这是登陆页面')


@csrf_exempt
def app_register(request):

    if request.method=='GET':
        return render(request,'post.html')
    else:
        req = json.loads(request.body)

        username = req['username']
        password = req['password']
        user_phone = req['phone']
        print(username, password, user_phone)
        if not all([username, user_phone, password]):
            data = {
                "status": '数据不完整'
            }
            return JsonResponse(data, json_dumps_params={'ensure_ascii':False})
        try:
            user = User.objects.get(Q(user_name=username) | Q(user_phone=user_phone))
        except User.DoesNotExist:
            user = None
        if user:
            data = {
                "status": '用户名已存在,或者手机号已存在'
            }
            return JsonResponse(data, json_dumps_params={'ensure_ascii':False})
        # 进行业务处理：进行用户注册@csrf_exempt
        user = User.objects.create_user(username=username, user_name=username, user_phone=user_phone, password=password)
        user.is_active = 1
        print('123')
        user.save()
        print("request.body={}".format(request.body))
        data = {
            "status": '200'
        }
        return JsonResponse(data, json_dumps_params={'ensure_ascii':False})