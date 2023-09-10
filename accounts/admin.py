from django.contrib import admin
from accounts.models import Department, Year, Profile, LoginHistory, Statistics


class YearAdmin(admin.ModelAdmin):
    search_fields = ['year']
    list_display = ['year', 'major_i', 'major_s', 'culture', 'culture_cnt', 'all']


class DepartmentAdmin(admin.ModelAdmin):
    search_fields = ['name', 'college', 'type']
    list_display = ['name', 'name', 'type']


class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['name', 'user__username', 'year__year', 'department__name']
    list_display = ['user', 'name', 'department']

class LoginHistoryAdmin(admin.ModelAdmin):
    search_fields = ['user__username']
    list_display = ['user', 'login_datetime']


class StatisticsAdmin(admin.ModelAdmin):
    search_fields = ['date']
    list_display = ['date', 'visit_count']


admin.site.register(Year, YearAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(LoginHistory, LoginHistoryAdmin)
admin.site.register(Statistics, StatisticsAdmin)
