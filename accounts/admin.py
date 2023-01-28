from django.contrib import admin
from accounts.models import Department, Year, Profile, LoginHistory

admin.site.register(Year)
admin.site.register(Department)
admin.site.register(Profile)
admin.site.register(LoginHistory)
