from django.conf.urls import url
from course.views_menu import *
from course.views import *
from enrol.views import *
from . import views

app_name = 'course'

urlpatterns = [

    url(r'^$', CourseLV.as_view(), name='index'),
    url(r'^course/$', CourseLV.as_view(), name='course_list'),
    url(r'^course/(?P<pk>\d+)/$', CourseDV.as_view(), name='course_detail'),
    url(r'^add/$',CourseScheduleCV.as_view(), name="add"),
    url(r'^change/$',CourseChangeLV.as_view(), name="change",),
    url(r'^(?P<pk>[0-9]+)/update/$',CourseUpdateView.as_view(), name="update",),
    url(r'^(?P<pk>[0-9]+)/delete/$',CourseDeleteView.as_view(), name="delete",),
    url(r'^like/$', views.like, name='like'),
    url(r'^likes/$',LikesLV.as_view(), name="likes",),
    url(r'^lecturer/(?P<pk>\d+)/$', LecturerDV.as_view(), name='lecturer'),
    #url(r'^lecturer/(?P<name_pk>\d+)/$', LecturerDV.as_view(), name='lecturer'),
    
    # course_lfield_list
    url(r'^lfield/1/$', CourseL1LV.as_view(), name='course_lfield_1_list'),
    url(r'^lfield/2/$', CourseL2LV.as_view(), name='course_lfield_2_list'),
    url(r'^lfield/3/$', CourseL3LV.as_view(), name='course_lfield_3_list'),
    url(r'^lfield/4/$', CourseL4LV.as_view(), name='course_lfield_4_list'),
    url(r'^lfield/5/$', CourseL5LV.as_view(), name='course_lfield_5_list'),
    url(r'^lfield/6/$', CourseL6LV.as_view(), name='course_lfield_6_list'),
    url(r'^lfield/7/$', CourseL7LV.as_view(), name='course_lfield_7_list'),

    # course_lfield_list
    url(r'^sfield/10/$', CourseS10LV.as_view(), name='course_sfield_10_list'),
    url(r'^sfield/11/$', CourseS11LV.as_view(), name='course_sfield_11_list'),
    url(r'^sfield/12/$', CourseS12LV.as_view(), name='course_sfield_12_list'),
    url(r'^sfield/13/$', CourseS13LV.as_view(), name='course_sfield_13_list'),
    url(r'^sfield/14/$', CourseS14LV.as_view(), name='course_sfield_14_list'),
    url(r'^sfield/15/$', CourseS15LV.as_view(), name='course_sfield_15_list'),
    url(r'^sfield/16/$', CourseS16LV.as_view(), name='course_sfield_16_list'),

    url(r'^sfield/20/$', CourseS20LV.as_view(), name='course_sfield_20_list'),
    url(r'^sfield/21/$', CourseS21LV.as_view(), name='course_sfield_21_list'),
    url(r'^sfield/22/$', CourseS22LV.as_view(), name='course_sfield_22_list'),
    url(r'^sfield/23/$', CourseS23LV.as_view(), name='course_sfield_23_list'),
    url(r'^sfield/24/$', CourseS24LV.as_view(), name='course_sfield_24_list'),
    url(r'^sfield/25/$', CourseS25LV.as_view(), name='course_sfield_25_list'),

    url(r'^sfield/30/$', CourseS30LV.as_view(), name='course_sfield_30_list'),
    url(r'^sfield/31/$', CourseS31LV.as_view(), name='course_sfield_31_list'),
    url(r'^sfield/32/$', CourseS32LV.as_view(), name='course_sfield_32_list'),
    url(r'^sfield/33/$', CourseS33LV.as_view(), name='course_sfield_33_list'),
    url(r'^sfield/34/$', CourseS34LV.as_view(), name='course_sfield_34_list'),
    url(r'^sfield/35/$', CourseS35LV.as_view(), name='course_sfield_35_list'),
    url(r'^sfield/36/$', CourseS36LV.as_view(), name='course_sfield_36_list'),

    url(r'^sfield/40/$', CourseS40LV.as_view(), name='course_sfield_40_list'),
    url(r'^sfield/41/$', CourseS41LV.as_view(), name='course_sfield_41_list'),
    url(r'^sfield/42/$', CourseS42LV.as_view(), name='course_sfield_42_list'),
    url(r'^sfield/43/$', CourseS43LV.as_view(), name='course_sfield_43_list'),
    url(r'^sfield/44/$', CourseS44LV.as_view(), name='course_sfield_44_list'),
    url(r'^sfield/45/$', CourseS45LV.as_view(), name='course_sfield_45_list'),
    url(r'^sfield/46/$', CourseS46LV.as_view(), name='course_sfield_46_list'),

    url(r'^sfield/50/$', CourseS50LV.as_view(), name='course_sfield_50_list'),
    url(r'^sfield/51/$', CourseS51LV.as_view(), name='course_sfield_51_list'),
    url(r'^sfield/52/$', CourseS52LV.as_view(), name='course_sfield_52_list'),

    url(r'^sfield/60/$', CourseS60LV.as_view(), name='course_sfield_60_list'),
    url(r'^sfield/61/$', CourseS61LV.as_view(), name='course_sfield_61_list'),
    url(r'^sfield/62/$', CourseS62LV.as_view(), name='course_sfield_62_list'),
    url(r'^sfield/63/$', CourseS63LV.as_view(), name='course_sfield_63_list'),
    url(r'^sfield/64/$', CourseS64LV.as_view(), name='course_sfield_64_list'),

    url(r'^sfield/70/$', CourseS70LV.as_view(), name='course_sfield_70_list'),

]