from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CourseUser(models.Model):
    role = CharField()          # Errr... should we use this?
    global_account = ForeignKey('User', on_delete=models.CASCADE)

class UnitType(models.Model): # Control work, Lecture, etc.
    name = CharField()

class CourseUnit(models.Model):
    name = CharField()          # Defines topic of a unit
    description = TextField()   # Here goes some description
    unit_type = ForeignKey('UnitType', on_delete=models.SET_NULL)

class Course(models.Model):
    name = CharField()
    description = TextField()  
    lecturer = ForeignKey('CourseUser', on_delete=models.SET_NULL)
    students = ManyToManyField('CourseUser')
    program = ManyToManyField('CourseUnit')
