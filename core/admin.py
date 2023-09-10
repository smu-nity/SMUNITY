from django.contrib import admin
from core.models import Course


class CourseAdmin(admin.ModelAdmin):
    search_fields = ['user__username', 'subject__number']
    list_display = ['subject', 'user', 'year', 'semester', 'credit', 'type', 'domain', 'custom']


admin.site.register(Course, CourseAdmin)
