from django.conf.urls import include, url
from university.student.ListView import Student_Course
from university.student import enrollment

urlpatterns = [
   url(r'student/(?P<pk>\d+)$', Student_Course.as_view(), name="course_list"),
   url(r'student/enrollment/$', enrollment.enrollment, name="enrollment"),
   url(r'student/enroll/(?P<pk>\d+)$', enrollment.enroll, name="enroll"),
   url(r'student/course_list/$', enrollment.course_list, name="courses"),                       
]

