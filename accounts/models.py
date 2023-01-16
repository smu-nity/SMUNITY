from django.contrib.auth.models import User
from django.db import models

DEPARTMENT_CHOICES = (("컴퓨터과학전공", "컴퓨터과학전공"), )
YEAR_CHOICES = (("2019", "19학번"), ("2020", "20학번"), ("2021", "21학번"), ("2022", "22학번"), ("2023", "23학번"))


class Year(models.Model):
    year = models.CharField(max_length=4, choices=YEAR_CHOICES)
    major = models.IntegerField()
    culture_e = models.IntegerField()
    culture_s = models.IntegerField()
    all = models.IntegerField()

    def __str__(self):
        return self.year


class Department(models.Model):
    name = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)

    def __str__(self):
        return f'[{self.year}] {self.user} {self.name} - {self.department}'
