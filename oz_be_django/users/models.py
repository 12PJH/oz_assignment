from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    # ====================================================
    # name = models.CharField(max_length=100)
    # description = models.TextField()
    # age = models.PositiveIntegerField(null=True)
    # gender = models.CharField(max_length=5)
    #
    # def __str__(self):
    #     return f"{self.name} / {self.age}살"
    # ===================================================
    in_business = models.BooleanField(default=False)
    grade = models.CharField(max_length=10, default='C')
