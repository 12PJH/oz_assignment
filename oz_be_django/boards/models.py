from django.db import models
from common.models import CommonModel


# Create your models here.
# 게시글에 들어갈 테이블
# - title
# - content
# - date
# - likes
# - reviews
class Board(CommonModel):
    title = models.CharField(max_length=50)
    content = models.TextField()
    writer = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    reviews = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title