from django.conf.urls import patterns, include, url
from university.student.ListView import Student_Course

urlpatterns = patterns('',
                       url(r'student/(?P<pk>\d+)$', Student_Course.as_view(), name="course_list"),
                       url(r'student/enrollment/$', 'university.student.enrollment.enrollment', name="enrollment"),
                       url(r'student/enroll/(?P<pk>\d+)$', 'university.student.enrollment.enroll', name="enroll"),
                       url(r'student/course_list/$', 'university.student.enrollment.course_list', name="courses"),
                       )