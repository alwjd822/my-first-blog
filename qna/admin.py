from django.contrib import admin
from qna.models import Qna

# Register your models here.

class QnaAdmin(admin.ModelAdmin):
    list_display  = ('owner','title','createdate','modifydate')
    list_display_links = ('owner','title') # 목록 내에서 링크로 지정할 필드 목록
    list_filter = ('owner', 'createdate')
    search_fields = ('details', 'id', 'owner', 'owner_id', 'title')
    list_per_page = 10 # 페이지 별로 보여질 최대 갯수

admin.site.register(Qna, QnaAdmin)
