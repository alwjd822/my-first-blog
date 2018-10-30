from django.conf.urls import url

from interest.views import *

app_name = 'interest'

urlpatterns = [

    url(r'^$', InterestLV.as_view(), name='index'),

    #url(r'^$', InterestLV.as_view(), name='interest_list'),

    url(r'^(?P<pk>\d+)/$', InterestDV.as_view(), name='interest_detail'),


]

