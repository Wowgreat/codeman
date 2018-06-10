from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'userAdd(添加用户)': reverse('users-add', request=request, format=format),
        'userAuth(用户登录)': reverse('user-auth', request=request, format=format),
        'userInfo(用户信息)': reverse('user-info', request=request, format=format),
        'groupInfo(小组信息)': reverse('group-info-by-id', request=request, format=format),
    })