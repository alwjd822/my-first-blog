from django.conf.urls import url
from lecturer.views import *

app_name = 'lecturer'

urlpatterns = [
    url(r'^$', LecturerLV.as_view(), name='index'),
    #url(r'^detail/(?P<course_pk>\d+)/$', LecturerDV.as_view(), name='lecturer'),
    url(r'^new/$',LecturerCreateView.as_view(), name="new"),
    url(r'^(?P<pk>[0-9]+)/update/$',LecturerUpdateView.as_view(), name="update",),
    url(r'^(?P<pk>[0-9]+)/delete/$',LecturerDeleteView.as_view(), name="delete",),

]