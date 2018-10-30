from django.conf.urls import url

from reply.views import *

app_name = 'reply'

urlpatterns = [

    # Example: /
    url(r'^$', ReplyLV.as_view(), name='index'),

    # Example: /album/, same as /
    url(r'^reply/$', ReplyLV.as_view(), name='reply_list'),

    # Example: /album/99/
    url(r'^reply/(?P<pk>\d+)/$', ReplyDV.as_view(), name='reply_detail'),

]

