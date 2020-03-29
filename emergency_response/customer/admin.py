from django.contrib import admin
from customer.models import CustomerDetails
# Register your models here.
from django.conf import settings


class StaffRequiredAdminMixin(object):

    def check_perm(self, user_obj):
        if user_obj.is_superuser:
            return True
        if not user_obj.is_active or user_obj.is_anonymous or user_obj.is_staff:
            return False
        return False

    def has_add_permission(self, request):
        return self.check_perm(request.user)

    def has_change_permission(self, request, obj=None):
        return self.check_perm(request.user)

    # def has_delete_permission(self, request, obj=None):
    #     return self.check_perm(request.user)

    def has_module_permission(self, request):
        return True


class CustomerDetailAdmin(StaffRequiredAdminMixin, admin.ModelAdmin):
    # readonly_fields = ('id', 'uid',
    #                    'name', 'phone_number', 'address', 'grocery',
    #                    'landmark')
    exclude = ('location', )

    def get_readonly_fields(Self, request, obj=None):
        if not request.user.is_superuser:
            return ('verfication_completed', 'uid',
                    'name', 'phone_number', 'address', 'grocery',
                    'landmark', 'updated_by')
        else:
            return ('uid',
                    'name', 'phone_number', 'address', 'grocery',
                    'landmark', 'updated_by')
    # def has_change_permission(self, request, obj=None):
    #     return True


admin.site.register(CustomerDetails, CustomerDetailAdmin)


class UnReachableDetailCustomerAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'uid',
                       'name', 'phone_number', 'address', 'grocery',
                       'landmark')

    def get_queryset(self, request):
        query = super(UnReachableDetailCustomerAdmin, self).get_queryset(request)
        data = query.filter(order_status=settings.UNREACHABLE_CUSTOMER)
        return data

    def has_add_permission(self, request):
        return False

    def has_module_permission(self, request):
        return True


class UnReachableCustomer(CustomerDetails):
    class Meta:
        proxy = True


admin.site.register(UnReachableCustomer, UnReachableDetailCustomerAdmin)