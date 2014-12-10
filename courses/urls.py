from django.conf.urls import patterns, url

from courses.views import courses_list, course_info


urlpatterns = patterns('',
                       url(r'^/(?P<course_id>\d+)/$', course_info,
                           name="course_info"),
                       url(r'^/$', courses_list, name='courses_list'),
                       )
