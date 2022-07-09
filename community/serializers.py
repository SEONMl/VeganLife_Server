from rest_framework import serializers as sz

from community.models import Article, Comment
from member.serializers import MemberSerializer


class ArticleSerializer(sz.Serializer):
    class Meta:
        model = Article

    writer = MemberSerializer()
    content = sz.CharField()
    like_count = sz.IntegerField(default=0)
    written_time = sz.DateTimeField()
    updated_time = sz.DateTimeField()
    community_code = sz.IntegerField()

    def update(self, instance, validated_data):
        return instance

    def create(self, validated_data):
        return Article.objects.create(**validated_data)


class CommentSerializer(sz.Serializer):
    class Meta:
        model = Comment

    article = ArticleSerializer()
    content = sz.CharField()
    like_count = sz.IntegerField(default=0)
    written_time = sz.DateTimeField()
    updated_time = sz.DateTimeField()
    writer = MemberSerializer()

    def update(self, instance, validated_data):
        return instance

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)
