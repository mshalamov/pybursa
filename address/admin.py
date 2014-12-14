from django.contrib import admin

from address.models import Address


class AddressAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'zip_code',
                    'country',
                    'province',
                    'district',
                    'street',
                    'house')
    list_filter = ['zip_code',
                   'country',
                   'province',
                   'district',
                   'street',
                   'house']
    search_fields = ['zip_code',
                     'country',
                     'province',
                     'district',
                     'street',
                     'house']
    short_description = ['id',
                         'zip_code',
                         'country',
                         'province',
                         'district',
                         'street',
                         'house']


admin.site.register(Address, AddressAdmin)
