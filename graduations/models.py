from django.contrib.auth.models import User
from django.db import models
from accounts.models import Department
from config.settings import TYPE_CHOICES, SUBTYPE_CHOICES_E, SUBTYPE_CHOICES_S, TYPE_NAMES, YEAR_CHOICES, \
    SEMESTER_CHOICES


class Type(models.Model):
    name = models.CharField(max_length=2, choices=(TYPE_NAMES))
    type = models.CharField(max_length=3, choices=TYPE_CHOICES)
    subtype = models.CharField(max_length=20, null=True, blank=True, choices=SUBTYPE_CHOICES_E+SUBTYPE_CHOICES_S)

    def __str__(self):
        return f'{self.name} - {self.type} - {self.subtype}'


class Subject(models.Model):
    number = models.CharField(max_length=10)
    ecampus = models.IntegerField()
    name = models.CharField(max_length=30)
    credit = models.IntegerField()
    dept = models.CharField(max_length=30)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    year = models.CharField(max_length=4, choices=YEAR_CHOICES)
    semester = models.CharField(max_length=2, choices=SEMESTER_CHOICES)

    def __str__(self):
        return f'[{self.ecampus}] {self.name}'


class Major(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    type = models.CharField(max_length=3, null=True, blank=True)

    def __str__(self):
        return f'[{self.department}] {self.subject}'
