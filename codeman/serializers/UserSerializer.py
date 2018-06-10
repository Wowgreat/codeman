from rest_framework import serializers
from codeman.models import User
from .GroupSerializer import GroupSerializer


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "name", "email", "password", "intro", "avatar", "occupation", "is_show_location", "company_or_school")
# class UserSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(required=False, allow_blank=True, max_length=100,default='未命名')
#     email = serializers.CharField(max_length=100)
#     password = serializers.CharField(max_length=100)
#     intro = serializers.CharField(max_length=300, allow_blank=True, default='略')
#
#     avatar = serializers.CharField(max_length=200, allow_blank=True,
#                               default='https://www.sucaijishi.com/uploadfile/2016/0203/20160203022635285.png')
#     occupation = serializers.CharField(max_length=100, allow_blank=True, default='保密')
#     is_show_location = serializers.BooleanField(default=False)
#     company_or_school = serializers.CharField(max_length=100, allow_blank=True, default='保密')
#
#     def create(self, validated_data):
#         """
#         Create and return a new `User` instance, given the validated data.
#         """
#         return User.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `User` instance, given the validated data.
#         """
#         instance.name = validated_data.get('name', instance.name)
#         instance.email = validated_data.get('email', instance.email)
#         instance.password = validated_data.get('password', instance.password)
#         instance.intro = validated_data.get('intro', instance.intro)
#         instance.avatar = validated_data.get('avatar', instance.avatar)
#         instance.occupation = validated_data.get('occupation', instance.occupation)
#         instance.is_show_location = validated_data.get('is_show_location', instance.is_show_location)
#         instance.company_or_school = validated_data.get('company_or_school', instance.company_or_school)
#         instance.save()
#         return instance