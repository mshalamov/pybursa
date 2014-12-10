from django.conf.urls import patterns, url

from students.views import student_info, students_list


urlpatterns = patterns('',
                       url(r'^/(?P<student_id>\d+)/$', student_info,
                           name="student_info"),
                       url(r'^/$', students_list, name='students_list'),
                       )
