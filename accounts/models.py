from django.contrib.auth.models import User
from django.db import models
from config.settings import YEAR_CHOICES, DEPARTMENT_CHOICES, SUBTYPE_CHOICES_S, COLLEGE_CHOICES


class Year(models.Model):
    year = models.CharField(max_length=4, choices=YEAR_CHOICES)
    major = models.IntegerField()
    culture_e = models.IntegerField()
    culture_s = models.IntegerField()
    all = models.IntegerField()

    def __str__(self):
        return self.year


class Department(models.Model):
    college = models.CharField(max_length=20, choices=COLLEGE_CHOICES)
    name = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)
    type = models.CharField(max_length=2, choices=SUBTYPE_CHOICES_S)
    def __str__(self):
        return f'[{self.college}] {self.name}'


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)

    def __str__(self):
        return f'[{self.year}] {self.user} {self.name} - {self.department}'
