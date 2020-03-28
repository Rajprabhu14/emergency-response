from django.contrib import admin
from customer.models import CustomerDetails
# Register your models here.


class CustomerDetailAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'uid',
                       'name', 'phone_number', 'address', 'grocery',
                       'landmark')
    exclude = ('location', )


admin.site.register(CustomerDetails, CustomerDetailAdmin)
