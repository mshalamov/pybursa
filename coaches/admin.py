from django.contrib import admin

from coaches.models import Coach


class CoachAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'coach_type')
    list_filter = ['first_name', 'last_name', 'coach_type']
    search_fields = ['first_name', 'last_name', 'coach_type']
    short_description = ['id', 'first_name', 'last_name', 'coach_type']
    radio_fields = {"coach_type": admin.HORIZONTAL}

admin.site.register(Coach, CoachAdmin)