from django.contrib import admin
from graduations.models import Subject, Major, Culture


class SubjectAdmin(admin.ModelAdmin):
    search_fields = ['number']


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Major)
admin.site.register(Culture)
