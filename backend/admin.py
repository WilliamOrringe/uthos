from django.contrib import admin

from backend.models import *


class UserAdmin(admin.ModelAdmin):
    list_filter = ("teacher_request",)


admin.site.register(User, UserAdmin)
