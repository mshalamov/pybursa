from django.contrib import admin

from students.models import Student, Dossier


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

admin.site.register(Student, StudentAdmin)


class DossierAdmin(admin.ModelAdmin):
    list_display = ('address', 'like_color')

admin.site.register(Dossier, DossierAdmin)