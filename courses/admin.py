from django.contrib import admin

# Register your models here.
from courses.models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'technology', 'start_date', 'end_date')

admin.site.register(Course, CourseAdmin)