from django.db import models

# Create your models here.
# 게시글에 들어갈 테이블
# - title
# - content
# - date
# - likes
# - reviews
class Board(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)