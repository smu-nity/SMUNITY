from django.contrib.auth.models import User
from django.db import models
from accounts.models import Department
from config.settings import TYPE_CHOICES, SUBTYPE_CHOICES_E, SUBTYPE_CHOICES_S


class Subject(models.Model):    # 과목 테이블
    number = models.CharField(max_length=10, unique=True)       # 학수번호
    name = models.CharField(max_length=100)  # 이름
    credit = models.IntegerField()          # 학점
    dept = models.CharField(max_length=100)  # 개설학부
    type = models.CharField(max_length=3, choices=TYPE_CHOICES) # 이수구분

    def __str__(self):
        return f'[{self.number}] {self.name}'


class Major(models.Model):      # 전공 과목 테이블
    department = models.ForeignKey(Department, on_delete=models.CASCADE)    # 학과
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)          # 과목
    grade = models.CharField(max_length=4)                                  # 학년
    semester = models.CharField(max_length=3)                               # 학기
    type = models.CharField(max_length=3)                                   # 이수구분

    def __str__(self):
        return f'[{self.department}] {self.subject}'


class Culture(models.Model):    # 교양 과목 테이블
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)                     # 과목
    type = models.CharField(max_length=2, choices=(('교필', '교필'), ('교선', '교선')))     # 이수구분
    domain = models.CharField(max_length=2, choices=(('핵심', '핵심'), ('균형', '균형')))   # 영역명
    subdomain = models.CharField(max_length=20, choices=SUBTYPE_CHOICES_E+SUBTYPE_CHOICES_S)    # 세부 영역명

    def __str__(self):
        return f'[{self.type} - {self.subdomain}] {self.subject}'
