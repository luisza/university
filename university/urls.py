from django.conf.urls import patterns, include, url
from university.student.ListView import Student_Course

urlpatterns = patterns('',
                       url(r'student/(?P<pk>\d+)$', Student_Course.as_view(), name="course_list"),
                       )