from rest_framework import permissions

# Not Auth - base permission AllowAny

# Student
class IsStudent(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.groups.filter(name='student'):
            return True
        return False

# Master Student
class IsMasterStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.groups.filter(name='master_student'):
            return True
        return False

# Teacher
class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.groups.filter(name='teacher'):
            return True
        return False

# Admin - base permission IsAdmin