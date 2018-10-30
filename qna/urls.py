"""from django.conf.urls import url

from qna.views import *

app_name = 'qna'

urlpatterns = [

    # Example: /
    url(r'^$', QnaLV.as_view(), name='index'),

    # Example: /album/, same as /
    url(r'^qna/$', QnaLV.as_view(), name='qna_list'),

    # Example: /album/99/
    url(r'^qna/(?P<pk>\d+)/$', QnaDV.as_view(), name='qna_detail'),

]
"""
from django.conf.urls import url

from qna.views import *

app_name = 'qna'

urlpatterns = [
    
    url(r'^$', PostLV.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', PostDV.as_view(), name='detail'),
    url(r'^add/$',PostCreateView.as_view(), name="add",),
    url(r'^change/$',PostChangeLV.as_view(), name="change",),
    url(r'^(?P<pk>[0-9]+)/update/$',PostUpdateView.as_view(), name="update",),
    url(r'^(?P<pk>[0-9]+)/delete/$',PostDeleteView.as_view(), name="delete",),

]

