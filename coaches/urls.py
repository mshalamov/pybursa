from django.conf.urls import patterns, url

from coaches.views import coaches_list, coach_info


urlpatterns = patterns('',
                       url(r'^/(?P<coach_id>\d+)/$', coach_info,
                           name="coach_info"),
                       url(r'^/$', coaches_list, name='coaches_list'),
                       )
