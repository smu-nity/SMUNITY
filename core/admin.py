from django.contrib import admin
from core.models import Course


class CourseAdmin(admin.ModelAdmin):
    search_fields = ['user__username', 'subject__number']


admin.site.register(Course, CourseAdmin)
