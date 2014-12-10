from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = patterns('',
                       url(r'^student', include('students.urls')),
                       url(r'^coach', include('coaches.urls')),
                       url(r'^course', include('courses.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$',
                           TemplateView.as_view(template_name='index.html'),
                           name='home'),
                       url(r'^persons$',
                           TemplateView.as_view(template_name='persons.html'),
                           name='persons'),
                       url(r'^person$',
                           TemplateView.as_view(template_name='person.html'),
                           name='home'))
