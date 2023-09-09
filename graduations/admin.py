from django.contrib import admin
from graduations.models import Subject, Major, Culture


class SubjectAdmin(admin.ModelAdmin):
    search_fields = ['number', 'name', 'dept']
    list_display = ['number', 'name', 'credit', 'dept', 'type']


class MajorAdmin(admin.ModelAdmin):
    search_fields = ['department__name', 'subject__number', 'subject__name', 'type']
    list_display = ['department', 'subject', 'grade', 'semester', 'type']


class CultureAdmin(admin.ModelAdmin):
    search_fields = ['subject__number', 'subject__name', 'type', 'domain', 'subdomain']
    list_display = ['subject', 'type', 'domain', 'subdomain']


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Major, MajorAdmin)
admin.site.register(Culture, CultureAdmin)
