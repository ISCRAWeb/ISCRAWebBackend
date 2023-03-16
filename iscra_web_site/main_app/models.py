from django.db import models
from django.contrib.auth.models import User

# Fe-Ti is responsible for bugs in this code

# ~ USER_GLOBAL_ROLE_LEN = 30

# ~ COURSE_ROLE_NAME_LEN = 20
# ~ COURSE_UNITTYPE_NAME_LEN = 20

# ~ COURSE_NAME_LEN = 40
# ~ COURSE_UNIT_NAME_LEN = 100

# ~ OCCASION_NAME_LEN = 100
# ~ NEWS_ARTICLE_NAME_LEN = 100

# User model extension

class GlobalUserRole(models.Model):
    # ~ name = models.CharField(USER_GLOBAL_ROLE_LEN)
    name = models.TextField(unique=True)

class AdditionalUserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roles = models.ManyToManyField(GlobalUserRole, blank=True)
    description = models.TextField()

# Course related models

class CourseRole(models.Model):
    # ~ name = CharField(max_length=COURSE_ROLE_NAME_LEN, unique=True)  # Defines a role of a user
    name = models.TextField(unique=True)  # Defines a role of a user

class CourseUser(models.Model):
    """
    CourseUser should be unique for each pair of Course and User.
    The object stores:
        roles           - a number of roles of the user
        global_account  - a ForeignKey to django.contrib.auth.models.User
    """
    roles = models.ManyToManyField(CourseRole)
    global_account = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)

class CourseUnitType(models.Model): # Control work, Lecture, etc.
    # ~ name = CharField(max_length=COURSE_UNITTYPE_NAME_LEN, unique=True)
    name = models.TextField(unique=True)

class CourseUnit(models.Model):
    # ~ name = CharField(max_length=COURSE_UNIT_NAME_LEN) # Defines topic of a unit
    name = models.TextField()          # Defines topic of a unit
    description = models.TextField()   # Here goes unit description
    unit_type = models.ForeignKey(
                                    CourseUnitType,
                                    on_delete=models.SET_NULL,
                                    blank=True,
                                    null=True
                                )

class CourseMaterial(models.Model):
    file_hash = models.TextField()
    available = models.BooleanField()
    # ~ course = models.ForeignKey(Course, on_delete=models.CASCADE)
    course_unit = models.ForeignKey(CourseUnit, on_delete=models.CASCADE)
    description = models.TextField()
    material = models.FileField(upload_to="uploads/materials/%Y/%m/%d/")

class Course(models.Model):
    # ~ name = CharField(max_length=COURSE_NAME_LEN)
    name = models.TextField()
    description = models.TextField()
    status = models.SmallIntegerField()        # Announced|Active|Finished
    available = models.BooleanField()          # Defines availability of registration
    lecturers = models.ManyToManyField(CourseUser, blank=True, related_name="lectured_courses")
    students = models.ManyToManyField(CourseUser, blank=True, related_name="studied_courses")
    program = models.ManyToManyField(CourseUnit, blank=True)
    materials = models.ManyToManyField(CourseMaterial, blank=True)

    date_of_adt =  models.DateTimeField(blank=True) ## date of announcement
    date_of_start =  models.DateTimeField(blank=True)
    date_of_end =  models.DateTimeField(blank=True)

# Other models

class Occasion(models.Model):
    # ~ name = CharField(max_length=OCCASION_NAME_LEN)
    name = models.TextField()
    description = models.TextField()
    date =  models.DateTimeField(blank=True)
    available = models.BooleanField()

class NewsArticle(models.Model):
    # ~ name = CharField(max_length=NEWS_ARTICLE_NAME_LEN)
    name = models.TextField()
    description = models.TextField()
    date =  models.DateTimeField(blank=True)
    available = models.BooleanField()
