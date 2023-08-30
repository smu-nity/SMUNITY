from django.db import models
from django.contrib.auth.models import User
from config.settings import STATUS_CHOICES, CATEGORY_CHOICES


class Petition(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_petition')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    category = models.IntegerField(choices=CATEGORY_CHOICES, default=1)
    anonymous = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True)
    voter = models.ManyToManyField(User, related_name='voter_question')
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    petition = models.ForeignKey(Petition, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(null=True, blank=True)


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='petition_answer')
    petition = models.ForeignKey(Petition, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(null=True, blank=True)
