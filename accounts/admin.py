from django.contrib import admin
from accounts.models import Department, Year, Profile


admin.site.register(Year)
admin.site.register(Department)
admin.site.register(Profile)
