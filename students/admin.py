# -*- coding: utf-8 -*-
from django.contrib import admin

from students.models import Student, Dossier


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    list_filter = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']
    short_description = ['id', 'first_name', 'last_name']
    radio_fields = {"package": admin.HORIZONTAL}

admin.site.register(Student, StudentAdmin)


class DossierAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'like_color')
    list_filter = ['address', 'like_color']
    search_fields = ['address', 'like_color']
    short_description = ['id', 'address', 'like_color']

admin.site.register(Dossier, DossierAdmin)