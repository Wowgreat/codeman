from codeman.models import Group, User
from codeman.serializers import GroupSerializer
from rest_framework.response import Response
from django.db import IntegrityError
from rest_framework.views import APIView
from .commonFunc import *
"""
create group
"""


class GroupAdd(APIView):
    serializer_class = GroupSerializer

    def get(self, request, format=None):
        return Response({"必要字段": "token,name,intro"})

    def post(self, request, format=None):
        formData = request.data
        userInfo = jwtdecode(formData.get('token'))
        if userInfo is False:
            return Response({"status": "ERROR", "msg": "token无效,请先登录,如有问题请联系管理员"})
        user = User.objects.get(id=userInfo.get('id'))
        try:
            group = user.created_groups.create(name=formData.get('name'), intro=formData.get('intro'))
        except IntegrityError:
            return Response({"status": "ERROR", "msg": "此名称已被占用,您可以搜索并加入，也可以更换小组名称"})
        group_serializer = GroupSerializer(group, many=False)
        return Response({"status": "OK", "msg": "创建小组成功", "data": group_serializer.data})


"""
get group by group_id
"""


class GroupInfoById(APIView):
    def get(self, request, format=None):
        return Response({"必要字段": "id(group id)"})

    def post(self, request, format=None):
        group_id = request.data.get('id')
        try:
            group = Group.objects.get(id=group_id)
        except Group.DoesNotExist:
            return Response({"status": "ERROR", "msg": "group id not exist"})
        group_serializer = GroupSerializer(group, many=False)
        return Response({"status": "OK", "data": group_serializer.data})


"""
查询用户参与的小组
"""


class GetGroupsByUser(APIView):
    def get(self, request, format=None):
        return Response({"必要字段": "查询他人参与的小组，需提供他人的id(user，id)；查询自己参与的小组需提供token"})

    def post(self, request, format=None):
        # 获取自己参与的小组
        if "token" in request.data:
            user_info = jwtdecode(request.get('token'))
            if user_info is False:
                return Response({"status": "ERROR", "msg": "token无效,请先登录,如有问题请联系管理员"})
            else:
                user = User.objects.get(id=user_info.get('id'))
        else:
            try:
                user = User.objects.get(id=request.data.get('id'))
            except User.DoesNotExist:
                return Response({"status": "ERROR", "msg": "请提供用户的有效id，或则是token"})
        groups = user.groups.all()
        groups_serializer = GroupSerializer(groups, many=True)
        return Response({"status": "OK", "data": groups_serializer.data})


"""
按名称搜索小组
"""