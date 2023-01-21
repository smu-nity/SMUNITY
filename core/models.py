from django.contrib.auth.models import User
from django.db import models
from config.settings import YEAR_CHOICES
from graduations.models import Subject


class Course(models.Model):     # 기이수과목 테이블
    user = models.ForeignKey(User, on_delete=models.CASCADE)        # 유저
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)  # 과목
    year = models.CharField(max_length=4, choices=YEAR_CHOICES)     # 이수 연도
    semester = models.CharField(max_length=20)  # 이수 학기
    credit = models.IntegerField()              # 학점
    type = models.CharField(max_length=3)       # 이수 구분
    domain = models.CharField(max_length=20, null=True, blank=True) # 교양 영역명
    custom = models.BooleanField(default=False)                     # 커스텀 유무

    def __str__(self):
        return f'[{self.user}] {self.subject}'
