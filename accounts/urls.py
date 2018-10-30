from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from accounts.views import *
from . import views

app_name = 'accounts'

urlpatterns = [
    
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/(?P<id>\d+)/edit/$', ProfileUpdateView.as_view(), name='profile_edit'),
    url(r'^(?P<pk>[0-9]+)/delete/$',ProfileDeleteView.as_view(), name="delete",),

    url(r'^login/$', auth_views.login, name='login', kwargs={'template_name': 'accounts/login_form.html'}),
    url(r'^logout/$', auth_views.logout, name='logout', kwargs={'next_page': settings.LOGIN_URL}),

    url(r'^password_reset/$', views.MyPasswordResetView.as_view(), name='password_reset'),
    url(r'^reset/<uidb64>/<token>/$', views.MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),

]

