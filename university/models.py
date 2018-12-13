from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

# https://docs.djangoproject.com/en/dev/ref/models/fields/

@python_2_unicode_compatible
class Student(models.Model):
    user = models.OneToOneField(User, related_name='student_of', verbose_name=_('User'), on_delete=models.CASCADE)
    enrollment_date = models.DateField(_('Enrollment Date'), auto_now_add=True)
    photo = models.ImageField(_('Photo'), upload_to='students')
    
    def __str__(self):
        return self.user.get_full_name()
    
    class Meta:
        verbose_name = _('Student')
        verbose_name_plural = _('Students')  
        
@python_2_unicode_compatible        
class Instructor(models.Model):
    user = models.OneToOneField(User, related_name='instructor_of', on_delete=models.CASCADE, verbose_name=_('User'))
    hire_date = models.DateField(_('Hire Date'), auto_now_add=True)
    office = models.ForeignKey('Office', on_delete=models.CASCADE, verbose_name=_('Office'))
    departament = models.ForeignKey('Departament',on_delete=models.CASCADE, verbose_name=_('Departament'))
    
    def __str__(self):
        return self.user.get_full_name()
    
    class Meta:
        verbose_name = _('Instructor')
        verbose_name_plural = _('Instructors')  

@python_2_unicode_compatible    
class Departament(models.Model):
    name = models.CharField(_('Name'), max_length=500)
    budget = models.FloatField(_('Budget'))
    start_date = models.DateField(_('Start Date'), auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Departament')
        verbose_name_plural = _('Departaments')  

@python_2_unicode_compatible  
class Course(models.Model):
    title = models.CharField(_('title'), max_length=500)
    credits = models.IntegerField(_('credits'), default=4)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, verbose_name=_('Instructor'))
    students = models.ManyToManyField(Student, verbose_name=_('Students'))

    def __str__(self):
        return self.title

    
    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')   

@python_2_unicode_compatible          
class Office(models.Model):
    location = models.SlugField(_('location'))

    def __str__(self):
        return self.location
       
    class Meta:
        verbose_name = _("Instructor office")
        verbose_name_plural = _("Instructor offices")   

