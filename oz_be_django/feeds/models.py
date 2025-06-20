from django.db import models
from common.models import CommonModel

# 제목(title), 내용(content), 작성자(User)
# User => Feed, Feed, Feed (o)
# Feed => User, User, User (x)
# User : Feed = 1(ForeignKey) : N
class Feed(CommonModel):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=300)

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)