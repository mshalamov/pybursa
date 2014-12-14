from django.contrib import admin

# Register your models here.
from courses.models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'technology', 'start_date', 'end_date')
    list_filter = ['name', 'technology', 'start_date', 'end_date']
    search_fields = ['name', 'technology', 'start_date', 'end_date']
    short_description = ['id', 'name', 'technology', 'start_date', 'end_date']
    radio_fields = {"technology": admin.HORIZONTAL}
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Course, CourseAdmin)