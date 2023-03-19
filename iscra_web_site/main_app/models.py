from django.db import models
from django.contrib.auth.models import User

# Fe-Ti is responsible for bugs in this code

#
# User model extension
#

class GlobalUserRole(models.Model):
    """
    Global user role. Usage - TBD (maybe in permissin system?)
    """
    name = models.TextField(unique=True)

class AdditionalUserInfo(models.Model):
    """
    Model for storing additional information about global user account.
    Currently has 3 fields:
        user        - OneToOne link to django.contrib.auth.models.User
        roles       - Global roles of that user
        description - Short description for that user
    """
    user = models.OneToOneField(
                                    User,
                                    on_delete=models.CASCADE
                                    )
    roles = models.ManyToManyField(
                                    GlobalUserRole,
                                    blank=True
                                    )
    description = models.TextField()

#
# Course related models
#

class CourseRole(models.Model):
    """
    TBD
    """
    name = models.TextField(unique=True)  # Defines a role of a user

class CourseUser(models.Model):
    """
    CourseUser should be unique for each pair of Course and User.
    The object stores:
        roles           - A number of roles of the user
        global_account  - A ForeignKey to django.contrib.auth.models.User
    """
    roles = models.ManyToManyField(CourseRole)
    global_account = models.ForeignKey(
                                        User,
                                        on_delete=models.CASCADE,
                                        unique=False
                                        )

class CourseUnitType(models.Model): # Control work, Lecture, etc.
    """
    Model for defining the type of unit in course program.
    E.g. lecture, seminar/workshop, control work and etc.
    """
    name = models.TextField(unique=True)

class CourseUnit(models.Model):
    """
    Units for use in course programs.
    Fields:
        name        - Unit name (topic)
        description - Unit description
        number      - Sequence number (for sorting, default = 0)
        unit_type   - Unit type, e.g. lecture, workshop and etc.
    """
    name = models.TextField()          # Defines topic of a unit
    description = models.TextField()   # Here goes unit description
    number = models.SmallIntegerField(default=0)
    unit_type = models.ForeignKey(
                                    CourseUnitType,
                                    on_delete=models.SET_NULL,
                                    blank=True,
                                    null=True
                                )

class CourseMaterial(models.Model):
    """
    This model represents files, which were uploaded by the course lecturer(-s).
    Available fields are:
        file_hash   - A hash sum of the file
        available   - Boolean field for setting visibility of the file
        course_unit - ForeignKey to the corresponding CourseUnit
        description - File desription
        material    - Actual link to the file
    """
    file_hash = models.TextField()
    available = models.BooleanField()
    course_unit = models.ForeignKey(
                                    CourseUnit,
                                    on_delete=models.CASCADE
                                    )
    description = models.TextField()
    material = models.FileField(
                                    upload_to="uploads/materials/%Y/%m/%d/"
                                    )

class Course(models.Model):
    """
    This model describes a single course.
    Fields are:
        name            - Course name
        description     - Course description
        status          - Small integer that corresponds to course status
        available       - Boolean for setting visibility
        users           - List of course users, i.e. lecturer and students
        program         - Course program
        materials       - Course materials
        date_of_adt     - Date of announcement
        date_of_start   - Date of start
        date_of_end     - Date of end
    """
    name = models.TextField()
    description = models.TextField()
    status = models.SmallIntegerField()        # Announced|Active|Finished
    available = models.BooleanField()          # Defines availability of registration

    users = models.ManyToManyField(
                                        CourseUser,
                                        blank=True
                                        )
    program = models.ManyToManyField(
                                        CourseUnit,
                                        blank=True
                                        )
    materials = models.ManyToManyField(
                                        CourseMaterial,
                                        blank=True
                                        )

    date_of_adt =  models.DateTimeField(blank=True) ## date of announcement
    date_of_start =  models.DateTimeField(blank=True)
    date_of_end =  models.DateTimeField(blank=True)

#
# Other models
#

class Occasion(models.Model):
    name = models.TextField()
    description = models.TextField()
    date =  models.DateTimeField(blank=True)
    available = models.BooleanField()

class NewsArticle(models.Model):
    name = models.TextField()
    description = models.TextField()
    date =  models.DateTimeField(blank=True)
    available = models.BooleanField()
