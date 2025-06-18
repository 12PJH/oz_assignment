from django.db import models

# Create your models here.
class CommonModel(models.Model):
    # auto_now_add = 현재 데이터 생성 시간을 기준으로 생성되는 데이터 // 이후 데이터가 업데이트 되어도 변경되지 않는다.
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now = 생성되는 시간 기준으로 일단 데이터가 생성된다. // 이후 업데이트가 진행되면 시간도 업데이트가 진행 완료된 시간으로 업데이트된다.
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # 데이터 베이스의 테이블에 위 클래스 안의 컬럼들이 저장되지 않는다.
        abstract = True