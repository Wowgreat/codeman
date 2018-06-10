from codeman.models import User
from codeman.serializers import UserSerializer
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import status
from django.db import IntegrityError
from rest_framework.views import APIView
from .commonFunc import jwtdecode, jwtencode
'''
添加用户
'''


class UserAdd(APIView):
    serializer_class = UserSerializer

    def get(self, request, format=None):
        return Response({"必要字段": "email,password"})
    """
    添加用户(注册用户)
    """

    def post(self, request, format=None):
        email = request.data.get('email')
        # 将密码转为密文
        password = make_password(request.data['password'], hasher='bcrypt')
        serializer = UserSerializer(data={'email': email, 'password': password})
        if serializer.is_valid():
            try:
                serializer.save()
            except IntegrityError:
                return Response({"status": "ERROR", "msg": "邮箱已被占用"})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


'''
用户验证
'''


class UserAuth(APIView):
    serializer_class = UserSerializer

    def get(self, request, format=None):
        return Response({"必要字段": 'email,password'})

    def post(self, request):
        try:
            user = User.objects.get(email=request.data.get('email'))
        except User.DoesNotExist:
            return Response({'status': 'ERROR', "msg": "该邮箱没有注册，请检查邮箱是否正确"})
        is_correct = check_password(password=request.data.get('password'), encoded=user.password)
        if is_correct:
            user_serializer = UserSerializer(user, many=False)
        else:
            return Response({"status": "ERROR", "msg": "密码错误"})
        token = jwtencode(user_serializer.data)
        return Response({"status": "OK", "token": token})


'''
获取用户基本信息
'''
class UserInfo(APIView):

    def get(self, request, format=None):
        return Response({"必要字段": 'token'})

    def post(self, request, format=None):
        user_info = jwtdecode(request.data.get('token'))
        if user_info:
            return Response({"status": "OK", "data": user_info})
        else:
            return Response({"status": "ERROR", "msg": "token无效,请先登录"})