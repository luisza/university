from django.conf.urls import  url 
from django.urls import path, include
from university.student.ListView import Student_Course, StudentList

urlpatterns = [
                path('student/', StudentList.as_view(), name="student_list"),
                url(r'student/(?P<pk>\d+)$', Student_Course.as_view(), name="course_list"),
              ]
