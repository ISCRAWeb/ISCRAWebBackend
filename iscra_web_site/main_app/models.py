from django.db import models
from django.contrib.auth.models import User
# Fe-Ti is responsible for bugs in this code

class CourseRole(models.Model):
    name = CharField()          # Defines topic of a unit

class CourseUser(models.Model):
    role = ForeignKey(CourseRoles, on_delete=models.SET_NULL)
    global_account = ForeignKey(User, on_delete=models.CASCADE)

class UnitType(models.Model): # Control work, Lecture, etc.
    name = CharField()

class CourseUnit(models.Model):
    name = CharField()          # Defines topic of a unit
    description = TextField()   # Here goes some description
    unit_type = ForeignKey(UnitType, on_delete=models.SET_NULL)

class CourseMaterial(models.Model):
    # hash = CharField()
    available = BooleanField()
    course_unit = ForeignKey(CourseUnit, on_delete=models.CASCADE)

class Course(models.Model):
    name = CharField()
    description = TextField()
    status = SmallIntegerField()        # Announced|Active|Finished
    available = BooleanField()          # Defines availability of registration
    lecturer = ForeignKey(CourseUser, on_delete=models.SET_NULL)
    students = ManyToManyField(CourseUser)
    program = ManyToManyField(CourseUnit)
    materials = ManyToManyField(CourseMaterial)

class Occasion(models.Model):
    name = CharField()
    description = TextField()  
    date =  models.DateTimeField(blank=True)
    available = BooleanField()

class NewsArticle(models.Model):
    name = CharField()
    description = TextField()  
    date =  models.DateTimeField(blank=True)
    available = BooleanField()
