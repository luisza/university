from django.views.generic import DetailView
from university.models import Student
from django.shortcuts import redirect, get_object_or_404

# https://docs.djangoproject.com/en/1.11/ref/class-based-views/generic-display/
# https://docs.djangoproject.com/en/1.11/ref/class-based-views/generic-editing/

class Student_Course(DetailView):
    model = Student
    
    def get(self, request, *args, **kwargs):
        pk = kwargs['pk'] # it is always str
        student = get_object_or_404(Student, user=request.user)
        if int(pk) == student.pk:
            return super(Student_Course, self).get(request, *args, **kwargs)
    
        return redirect('course_list', pk=student.pk)
    
    def get_queryset(self):
        query = super(Student_Course, self).get_queryset()
        return query.filter(user=self.request.user)
        

