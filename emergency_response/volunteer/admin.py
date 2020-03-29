from django.contrib import admin

from volunteer.models import Volunteer


# Register your models here.
class VolunteerAdmin(admin.ModelAdmin):
    readonly_fields = ('email', 'name', 'phone_number', 'address', 'uid')
    exclude = ('location', 'password', 'last_login', 'groups', 'permissions',
               'is_superuser', 'user_permissions', 'date_joined')


admin.site.register(Volunteer, VolunteerAdmin)
