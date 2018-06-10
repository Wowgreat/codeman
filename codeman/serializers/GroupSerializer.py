from codeman.models import Group
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=500, allow_blank=True, default='略')

    class Meta:
        model = Group
        fields = ("id", "name", "intro", "token", "create_man_id")