from django.shortcuts import redirect, get_object_or_404, render
from university.models import Student, Course
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django_ajax.decorators import ajax

@login_required
def enrollment(request):
   return render(request, 'university/enrollment.html')
    
@ajax
@login_required
def course_list(request):
    student = get_object_or_404(Student, user=request.user)
    courses = Course.objects.all().exclude(students=student)
    return {
             'inner-fragments': {
                '#courses_list': render_to_string('university/courses.html', {'courses': courses})
              }
            }
        
@ajax
@login_required
def enroll(request, pk):
    student = get_object_or_404(Student, user=request.user)
    course = get_object_or_404(Course, pk=pk)
    course.students.add(student)
    return {
            'inner-fragments': {
                '#message': render_to_string('university/success.html', {'course': course, 
                                                                         'student': student})
              }
            
            }