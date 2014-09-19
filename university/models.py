from django.db import models
from django.contrib.auth.models import User

# https://docs.djangoproject.com/en/dev/ref/models/fields/

class Student(models.Model):
    user = models.OneToOneField(User, related_name='student_of')
    enrollment_date = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to='students', width_field=413, height_field=531)
     

class Instructor(models.Model):
    user = models.OneToOneField(User, related_name='instructor_of')
    hire_date = models.DateField(auto_now_add=True)
    office = models.ForeignKey('Office')
    departament = models.ForeignKey('Departament')

class Departament(models.Model):
    name = models.CharField(max_length=500)
    budget = models.FloatField()
    start_date = models.DateField(auto_now_add=True)


class Course(models.Model):
    title = models.CharField(max_length=500)
    credits = models.IntegerField(default=4)
    instructor = models.ForeignKey(Instructor)
    students = models.ManyToManyField(Student)
    
class Office(models.Model):
    location = models.SlugField()