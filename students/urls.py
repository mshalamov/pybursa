from django.conf.urls import patterns, url

from students.views import student_info, students_list, student_edit, \
    student_add


urlpatterns = patterns('',
                       url(r'^/(?P<student_id>\d+)/$', student_info,
                           name="student_info"),
                       url(r'^/edit/(?P<student_id>\d+)/$', student_edit,
                           name="student_edit"),
                       url(r'^/$', students_list, name='students_list'),
                       url(r'^/add/$', student_add, name='students_add'),
                       )
