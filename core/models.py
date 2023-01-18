from django.contrib.auth.models import User
from django.db import models
from config.settings import YEAR_CHOICES
from graduations.models import Subject


class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    year = models.CharField(max_length=4, choices=YEAR_CHOICES)
    semester = models.CharField(max_length=20)
    credit = models.IntegerField()
    type = models.CharField(max_length=3)
    domain = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f'[{self.user}] {self.subject}'
