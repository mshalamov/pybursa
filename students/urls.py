from django.conf.urls import patterns, url

from students.views import student_list, student_item


urlpatterns = patterns('',
                       url(r'^$', student_list),
                       url(r'^(?P<student_id>\d+)/$', student_item))
