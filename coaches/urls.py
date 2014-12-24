from django.conf.urls import patterns, url

from coaches.views import coach_edit, coach_add, \
    CoachView, CoachListView


urlpatterns = patterns('',
                       url(r'^/(?P<coach_id>\d+)/$',
                           CoachView.as_view(),
                           name="coach_info"),
                       url(r'^/edit/(?P<coach_id>\d+)/$', coach_edit,
                           name="coach_edit"),
                       url(r'^/$',
                           CoachListView.as_view(),
                           name='coaches_list'),
                       url(r'^/add/$', coach_add, name='coach_add'),
                       )
