from distutils.sysconfig import customize_compiler
from django.contrib import admin
from .models import Userprofile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class UserProfileInLine(admin.StackedInline):
    model = Userprofile
    can_delete = False
    verbose_name_plural = 'UserProfiles'

class CustomizedUserAdmin (UserAdmin):
    inlines = (UserProfileInLine, )

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)

admin.site.register(Userprofile)