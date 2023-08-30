from django.contrib import admin
from petitions.models import Petition, Comment, Answer


admin.site.register(Petition)
admin.site.register(Comment)
admin.site.register(Answer)
