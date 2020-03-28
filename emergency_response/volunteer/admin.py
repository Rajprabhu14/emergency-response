from django.contrib import admin

from volunteer.models import Volunteer


# Register your models here.
class VolunteerAdmin(admin.ModelAdmin):
    readonly_fields = ('email', 'name', 'phone_number', 'address',)
    exclude = ('location', 'password', 'last_login', 'uid')


admin.site.register(Volunteer, VolunteerAdmin)
