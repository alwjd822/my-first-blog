from course.models import Course, Schedule, Gallery
from django.forms.models import inlineformset_factory

ScheduleInlineFormSet = inlineformset_factory(Course, Schedule,
    fields = ['starttime', 'endtime'],
    extra = 1)

ScheduleUVInlineFormSet = inlineformset_factory(Course, Schedule,
    fields = ['starttime', 'endtime'],
    extra = 0)

GalleryInlineFormSet = inlineformset_factory(Course, Gallery,
    fields = ['image1', 'image2', 'image3', 'image4'],
    extra = 1)

GalleryUVInlineFormSet = inlineformset_factory(Course, Gallery,
    fields = ['image1', 'image2', 'image3', 'image4'],
    extra = 0)