from django.contrib import admin

from address.models import Address


class AddressAdmin(admin.ModelAdmin):
    list_display = ('zip_code',
                    'country',
                    'province',
                    'district',
                    'street',
                    'house')

admin.site.register(Address, AddressAdmin)
