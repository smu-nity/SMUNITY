from django.contrib.auth.models import User
from django.db import models
from accounts.models import Department

TYPE_CHOICES = (("핵심", "핵심"), ("기초", "기초"), ("균형", "균형"), ("일반", "일반"), ("1전선", "1전선"), ("1전심", "1전심"), ("1교직", "1교직"), ("1전필", "1전필"),  ("일선", "일선"))
SUBTYPE_CHOICES_E = (("창의적문제해결역량", "창의적문제해결역량"), ("융복합역량", "융복합역량"), ("다양성존중역량", "다양성존중역량"), ("윤리실천역량", "윤리실천역량"))
SUBTYPE_CHOICES_S = (("인문", "인문"), ("사회", "사회"), ("자연", "자연"), ("공학", "공학"), ("예술", "예술"))


class Type(models.Model):
    name = models.CharField(max_length=2, choices=(("교필", "교필"), ("교선", "교선"), ("전공", "전공")))
    type = models.CharField(max_length=3, choices=TYPE_CHOICES)
    subtype = models.CharField(max_length=20, null=True, blank=True, choices=SUBTYPE_CHOICES_E+SUBTYPE_CHOICES_S)

    def __str__(self):
        return f'{self.name} - {self.type} - {self.subtype}'


class Subject(models.Model):
    number = models.CharField(max_length=10)
    ecampus = models.IntegerField
    name = models.CharField(max_length=30)
    credit = models.IntegerField
    dept = models.CharField(max_length=30)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.ecampus}] {self.name}'


class Major(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    type = models.CharField(max_length=3, null=True, blank=True)

    def __str__(self):
        return f'[{self.department}] {self.subject}'
