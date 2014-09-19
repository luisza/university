from django.contrib import admin

# Register your models here.

from university.models import Student, Instructor, Course, Departament, Office

admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(Departament)
admin.site.register(Office)


