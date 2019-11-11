from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# https://docs.djangoproject.com/en/dev/ref/models/fields/

class Student(models.Model):
    user = models.OneToOneField(User, related_name='student_of', verbose_name=_('User'), on_delete=models.CASCADE)
    enrollment_date = models.DateField(_('Enrollment Date'), auto_now_add=True)
    photo = models.ImageField(_('Photo'), upload_to='students')
      
    class Meta:
        verbose_name = _('Student')
        verbose_name_plural = _('Students')  
        
class Instructor(models.Model):
    user = models.OneToOneField(User, related_name='instructor_of', on_delete=models.CASCADE, verbose_name=_('User'))
    hire_date = models.DateField(_('Hire Date'), auto_now_add=True)
    office = models.ForeignKey('Office', on_delete=models.CASCADE, verbose_name=_('Office'))
    departament = models.ForeignKey('Departament',on_delete=models.CASCADE, verbose_name=_('Departament'))
    
    class Meta:
        verbose_name = _('Instructor')
        verbose_name_plural = _('Instructors')  
        
class Departament(models.Model):
    name = models.CharField(_('Name'), max_length=500)
    budget = models.FloatField(_('Budget'))
    start_date = models.DateField(_('Start Date'), auto_now_add=True)
    
    class Meta:
        verbose_name = _('Departament')
        verbose_name_plural = _('Departaments')  
        indexes = [
            models.Index(fields=['name', 'budget']),
        ]
 
class Course(models.Model):
    title = models.CharField(max_length=500)
    credits = models.IntegerField(default=4)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    
    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')   
        ordering = ['-title']

class Office(models.Model):
    location = models.SlugField(_('location'))
    
    class Meta:
        verbose_name = _("Instructor office")
        verbose_name_plural = _("Instructor offices")   

