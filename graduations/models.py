from django.contrib.auth.models import User
from django.db import models
from accounts.models import Department
from config.settings import TYPE_CHOICES, SUBTYPE_CHOICES_E, SUBTYPE_CHOICES_S


class Subject(models.Model):
    number = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    credit = models.IntegerField()
    dept = models.CharField(max_length=30)
    type = models.CharField(max_length=3, choices=TYPE_CHOICES)

    def __str__(self):
        return f'[{self.number}] {self.name}'


class Major(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    type = models.CharField(max_length=3, choices=(('1전선', '1전선'), ('1전심', '1전심')))

    def __str__(self):
        return f'[{self.department}] {self.subject}'


class Culture(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=(('교필', '교필'), ('교선', '교선')))
    domain = models.CharField(max_length=2, choices=(('핵심', '핵심'), ('기초', '기초'), ('균형', '균형'), ('일반', '일반')))
    subdomain = models.CharField(max_length=20, choices=SUBTYPE_CHOICES_E+SUBTYPE_CHOICES_S)

    def __str__(self):
        return f'[{self.type}] {self.subject}'
