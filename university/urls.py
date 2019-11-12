
from django.conf.urls import url
from django.urls import path, include
from university.student.ListView import Student_Course, StudentList
from university.student import enrollment

urlpatterns = [
   path('student/', StudentList.as_view(), name="student_list"),
   url(r'student/(?P<pk>\d+)$', Student_Course.as_view(), name="course_list"),
   url(r'student/enrollment/$', enrollment.enrollment, name="enrollment"),
   url(r'student/enroll/(?P<pk>\d+)$', enrollment.enroll, name="enroll"),
   url(r'student/course_list/$', enrollment.course_list, name="courses"),                       
]

