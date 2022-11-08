from django.db import models
from django.contrib.auth.models import User
# Fe-Ti is responsible for bugs in this code

# ~ COURSE_ROLE_NAME_LEN = 20
# ~ COURSE_UNITTYPE_NAME_LEN = 20

# ~ COURSE_NAME_LEN = 40
# ~ COURSE_UNIT_NAME_LEN = 100

# ~ OCCASION_NAME_LEN = 100
# ~ NEWS_ARTICLE_NAME_LEN = 100

# Course related models

class CourseRole(models.Model):
    # ~ name = CharField(max_length=COURSE_ROLE_NAME_LEN, unique=True)  # Defines a role of a user
    name = TextField(unique=True)  # Defines a role of a user

class CourseUser(models.Model):
    """
    CourseUser should be unique for each pair of Course and User.
    The object stores:
        roles           - a number of roles of the user
        global_account  - a ForeignKey to django.contrib.auth.models.User
    """
    roles = ManyToManyField(CourseRoles)
    global_account = ForeignKey(User, on_delete=models.CASCADE, unique=False)

class CourseUnitType(models.Model): # Control work, Lecture, etc.
    # ~ name = CharField(max_length=COURSE_UNITTYPE_NAME_LEN, unique=True)
    name = TextField(unique=True)

class CourseUnit(models.Model):
    # ~ name = CharField(max_length=COURSE_UNIT_NAME_LEN) # Defines topic of a unit
    name = TextField()          # Defines topic of a unit
    description = TextField()   # Here goes unit description
    unit_type = ForeignKey(UnitType, on_delete=models.SET_NULL)

class CourseMaterial(models.Model):
    file_hash = TextField()
    available = BooleanField()
    course = ForeignKey(Course, on_delete=models.CASCADE)
    course_unit = ForeignKey(CourseUnit, on_delete=models.CASCADE)
    description = TextField()
    material = FileField(upload_to="uploads/materials/%Y/%m/%d/")

class Course(models.Model):
    # ~ name = CharField(max_length=COURSE_NAME_LEN)
    name = TextField()
    description = TextField()
    status = SmallIntegerField()        # Announced|Active|Finished
    available = BooleanField()          # Defines availability of registration
    lecturers = ManyToManyField(CourseUser, blank=True)
    students = ManyToManyField(CourseUser, blank=True)
    program = ManyToManyField(CourseUnit, blank=True)
    materials = ManyToManyField(CourseMaterial, blank=True)

# Other models

class Occasion(models.Model):
    # ~ name = CharField(max_length=OCCASION_NAME_LEN)
    name = TextField()
    description = TextField()  
    date =  models.DateTimeField(blank=True)
    available = BooleanField()

class NewsArticle(models.Model):
    # ~ name = CharField(max_length=NEWS_ARTICLE_NAME_LEN)
    name = TextField()
    description = TextField()  
    date =  models.DateTimeField(blank=True)
    available = BooleanField()
