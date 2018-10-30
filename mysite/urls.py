from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static # 추가
from django.conf import settings # 추가

from mysite.views import HomeView, SiteView , MypageView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView # 추가



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls',namespace='accounts')),
    url(r'^$', HomeView.as_view(), name='home'), # 추가  ^$ 은 Empty string을 표현하는데, / 혹은 현재위치에 해당된다.
    url(r'^home/', SiteView.as_view(), name='sitemap'),
    url(r'^qna/', include('qna.urls', namespace='qna')),
    url(r'^accounts/mypage/$', MypageView.as_view(), name='mypage'),
    url(r'^notice/', include('notice.urls', namespace='notice')),
    url(r'^course/', include('course.urls', namespace='course')),
    url(r'^interest/', include('interest.urls', namespace='interest')),
    url(r'^reply/', include('reply.urls', namespace='reply')),
    url(r'^enrol/', include('enrol.urls', namespace='enrol')),
    url(r'^lecturer/', include('lecturer.urls', namespace='lecturer')),

    url(r'^password_change/', PasswordChangeView.as_view(), name='password_change', kwargs={'next_page': settings.LOGIN_URL}),
    url(r'^password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),

    url(r'^password_reset/', PasswordResetView.as_view(), name='password_reset'),
    url(r'^password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
 
