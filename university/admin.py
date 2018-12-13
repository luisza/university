from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from university.models import Student, Instructor, Course, Departament, Office

class Student_Admin(admin.ModelAdmin):
    search_fields = ('user__first_name', 'user__last_name')
    list_display = ('view_foto', '__str__', 'enrollment_date', 'photo', 'credits' )
    date_hierarchy = 'enrollment_date'
    list_per_page = 10

    def view_foto(self, obj):
        return mark_safe('<img src="%s" width="40px" height="50px"/>' % obj.photo.url)
    view_foto.short_description = _("Photo image")
    view_foto.allow_tags = True
    
    def credits(self, obj):
        return sum(map(int, [course['credits'] for course in obj.course_set.all().values('credits')]))
    
    credits.short_description = _("Credits")

class Course_Admin(admin.ModelAdmin):
    filter_horizontal = ('students', )
    list_filter = ('instructor', 'instructor__departament')
    
    actions = ('unsubscribe_student', )
    
    def unsubscribe_student(self, request, queryset):
        for curse in queryset:
            curse.students.clear()
        self.message_user(request, _("Ok, User unsubscribe"))
    unsubscribe_student.short_description = _('Unsubscribe Students')
    
class Instructor_Admin_inline(admin.StackedInline):
    model = Instructor
    extra = 1
        
class Departament_Admin(admin.ModelAdmin):
    inlines = (Instructor_Admin_inline, )

    
admin.site.register(Student, Student_Admin)
admin.site.register(Course, Course_Admin)
#admin.site.register(Instructor)
admin.site.register(Departament, Departament_Admin)
admin.site.register(Office)


