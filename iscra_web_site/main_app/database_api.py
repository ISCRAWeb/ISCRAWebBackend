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
    return models.CourseUser.filter(global_account=django_user).filter(course_set=[course])

def is_registered(course, django_user):
    """
    
    """
    course_students = course.students.all().filter(global_account=django_user)
    course_lecturers = course.lecturers.all().filter(global_account=django_user)
    return (course_students.exists() or course_lecturers.exists())

def create_course_user(django_user, roles):
    """
    Function creates CourseUser object (with saving it to the database).
    """
    new_course_user = models.CourseUser(global_account=django_user)
    new_course_user.save()
    new_course_user.roles.add(roles)
    return new_course_user

def add_student(django_user, course, role):
    """
    Add student to the course.
    """
    if is_registered(course, django_user):
        raise AlreadyRegistered('Student is already registered. ')
    new_student = create_course_user(django_user, role)

def add_lecturer(django_user, course, role):
    """
    Add lecturer to the course.
    """
    if is_registered(course, django_user):
        raise AlreadyRegistered('Lecturer is already registered. ')
    new_lecturer = create_course_user(django_user, role)


def update_user_roles(django_user, course, roles, reset=False):
    """
    
    """
    course_user = get_course_user_object(course, django_user)
    if reset:
        
    course_user.roles.add(roles)

# ~ def create_course():
    

# ~ def create_course_unit():
    
    
# ~ def create_course_role(name):
    # ~ models.CourseRole.objects.create(name=name)

# ~ def create_course_material():
    
# ~ def create_course_user():
    
