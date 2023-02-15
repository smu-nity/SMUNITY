from django.contrib import admin
from graduations.models import Subject, Major, Culture


class SubjectAdmin(admin.ModelAdmin):
    search_fields = ['number', 'name', 'dept']


class MajorAdmin(admin.ModelAdmin):
    search_fields = ['department__name', 'subject__number', 'subject__name', 'type']


class CultureAdmin(admin.ModelAdmin):
    search_fields = ['subject__number', 'subject__name', 'type', 'domain', 'subdomain']


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Major, MajorAdmin)
admin.site.register(Culture, CultureAdmin)
