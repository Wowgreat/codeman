from codeman.models import Article
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=500, allow_blank=True, default='略')

    class Meta:
        model = Article
        fields = ("id", "token", "title", "content", "group", 'post_man', "helped_number", "is_show", "updated_at")