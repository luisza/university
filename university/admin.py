from django.contrib import admin

# Register your models here.

from university.models import Student, Instructor, Course, Departament, Office

class Student_Admin(admin.ModelAdmin):
    list_display = ('__str__', 'enrollment_date', 'photo' )
    date_hierarchy = 'enrollment_date'


class Course_Admin(admin.ModelAdmin):
    filter_horizontal = ('students', )
    
admin.site.register(Student, Student_Admin)
admin.site.register(Course, Course_Admin)
admin.site.register(Instructor)
admin.site.register(Departament)
admin.site.register(Office)


