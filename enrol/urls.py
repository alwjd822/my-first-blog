from django.conf.urls import url

from enrol.views import *

app_name = 'enrol'

urlpatterns = [

    url(r'^$', EnrolLV.as_view(), name='index'),
    #url(r'^enrol/(?P<pk>\d+)/$', EnrolDV.as_view(), name='enrol_detail'),
    url(r'^(?P<course_pk>\d+)/add/$',EnrolCreateView.as_view(), name="add"),
    #url(r'^change/$',EnrolChangeLV.as_view(), name="change",),
    url(r'^student/$', EnrolStudentLV.as_view(), name='enrol_student'),

]
