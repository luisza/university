from django.db import models
from django.contrib.auth.models import User

# https://docs.djangoproject.com/en/dev/ref/models/fields/

class Student(models.Model):
    user = models.OneToOneField(User, related_name='student_of', on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to='students', null=True)
     

class Instructor(models.Model):
    user = models.OneToOneField(User, related_name='instructor_of', on_delete=models.CASCADE)
    hire_date = models.DateField(auto_now_add=True)
    office = models.ForeignKey('Office', on_delete=models.CASCADE)
    departament = models.ForeignKey('Departament', on_delete=models.CASCADE)

class Departament(models.Model):
    name = models.CharField(max_length=500)
    budget = models.FloatField()
    start_date = models.DateField(auto_now_add=True)

    class Meta: 
        indexes = [
            models.Index(fields=['name', 'budget']),
        ]

class Course(models.Model):
    title = models.CharField(max_length=500)
    credits = models.IntegerField(default=4)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)

    class Meta:
        ordering = ['-title']
 
    
class Office(models.Model):
    location = models.SlugField()
