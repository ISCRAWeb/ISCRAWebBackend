import json

from . import models


# Course manipulation API

# # Exceptions
class AlreadyRegistered(Exception):
    """
    Custom exception.
    """
    pass

def get_course_user_object(course, django_user):
    """
    Get CourseUser object from course and global account.
    """
    return models.CourseUser.filter(global_account=django_user).filter(course_set__in=course)

def is_registered(course, django_user):
    """!
    Check if a user is registered on course.
    """
    course_students = course.students.all().filter(global_account=django_user)
    course_lecturers = course.lecturers.all().filter(global_account=django_user)
    return (course_students.exists() or course_lecturers.exists())

def create_course_user(django_user, roles):
    """!
    Function creates CourseUser object (with saving it to the database).
    """
    new_course_user = models.CourseUser.objects.create(global_account=django_user)
    new_course_user.roles.add(roles)
    return new_course_user

def add_student(django_user, course, role):
    """!
    Add student to the course.
    """
    if is_registered(course, django_user):
        raise AlreadyRegistered('Student is already registered. ')
    new_student = create_course_user(django_user, role)
    return new_student

def add_lecturer(django_user, course, role):
    """!
    Add lecturer to the course.
    """
    if is_registered(course, django_user):
        raise AlreadyRegistered('Lecturer is already registered. ')
    new_lecturer = create_course_user(django_user, role)
    return new_lecturer

def create_course(  name,
                    description,
                    status,
                    available,
                    lecturers=None,
                    students=None,
                    program=None,
                    materials=None):
    """!
    Add new Course. "Name", "description", "status" and "available"
    are mandatory parameters.
    """
    new_course = models.Course.objects.create(name=name,
                    description=description,
                    status=status,
                    available=available
                    )
    if lecturers:
        new_course.lecturers.add(lecturers)
    if students:
        new_course.students.add(students)
    if program:
        new_course.program.add(program)
    if materials:
        new_course.materials.add(materials)
    return new_course

def create_unit_type(name):
    """!
    Add new CourseUnitType.
    """
    new_course_unit_type = models.CourseUnitType.objects.create(name=name)
    return new_course_unit_type

def create_course_unit(name, description, unit_type):
    """!
    Add new CourseUnit.
    """
    new_course_unit = models.CourseUnit.objects.create(name=name, description=description, unit_type=unit_type)

def create_course_role(name):
    """!
    Add new CourseRole.
    """
    new_course_role = models.CourseRole.objects.create(name=name)

# ~ def create_course_material():

# ~ def delete_course_user(django_user, course):
    
# ~ def delete_course(course):
    
# ~ def delete_course_unit():
    
# ~ def delete_course_unit_type():
    
# ~ def delete_course_role():
    

def update_user_roles(django_user, course, roles, reset=False):
    """!
    Update user roles. If 'reset' is True then old roles are replaced with new.
    """
    course_user = get_course_user_object(course, django_user)
    if reset:
        course_user.roles.clear()
    course_user.roles.add(roles)
