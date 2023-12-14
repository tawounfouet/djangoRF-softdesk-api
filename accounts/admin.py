from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

 
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ["age", "consent_choice"]}),)
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ["age", "consent_choice"]}),
    )
 


admin.site.register(CustomUser, CustomUserAdmin)
