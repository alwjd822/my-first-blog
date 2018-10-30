from django.conf.urls import url

from notice.views import *

app_name = 'notice'

urlpatterns = [

    url(r'^$', NoticeLV.as_view(), name='index'),

    url(r'^notice/$', NoticeLV.as_view(), name='notice_list'),

    url(r'^notice/(?P<pk>\d+)/$', NoticeDV.as_view(), name='notice_detail'),

]
"""
from django.conf.urls import url
#from notice.views import NoticeLV, NoticeDV
from notice.views import *

app_name = 'notice'

urlpatterns = [
    # Class-based views
    #url(r'^$', NoticeLV.as_view(), name='index'),
    #url(r'^notice/$', NoticeLV.as_view(), name='notice'),
    #url(r'^(?P<pk>\d+)/$', NoticeDV.as_view(), name='detail'),
    #url(r'^notice.html/', TemplateView.as_view(template_name="notice.html")),
    url(r'^notice/', NoticeView.as_view(), name='notice'),
]
"""
