from django.contrib.auth.models import User
from django.db import models
from graduations.models import Subject


class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.user}] {self.subject}'
