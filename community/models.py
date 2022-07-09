from django.db import models


# Create your models here.


# 0 고민 worries, 1 챌린지 challenge, 2 레시피 recipe, 3 일상 dailylife
class Article(models.Model):
    class Meta:
        db_table = 'article'

    writer = models.ForeignKey('member.Member', on_delete=models.CASCADE, null=True)
    content = models.TextField()
    like_count = models.IntegerField(default=0)
    written_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True, null=True)
    community_code = models.IntegerField()


class Comment(models.Model):
    class Meta:
        db_table = 'comment'

    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    content = models.TextField()
    like_count = models.IntegerField(default=0)
    written_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True, null=True)
    writer = models.ForeignKey('member.Member', on_delete=models.CASCADE, null=True)


'''
class ArticleLikes(models.Model):
    class Meta:
        db_table = 'article_likes'

    article_id = models.ForeignKey('Article', on_delete=models.CASCADE)
    user_id = models.ForeignKey('member.Member', on_delete=models.CASCADE)


class CommentLikes(models.Model):
    class Meta:
        db_table = 'comment_likes'
    comment_id=models.ForeignKey('Comment', on_delete=models.CASCADE)
    user_id=models.ForeignKey('member.Member', on_delete=models.CASCADE)
'''
