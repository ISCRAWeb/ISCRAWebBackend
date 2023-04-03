from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import CourseUser, AdditionalUserInfo
from .serializers import *


@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = authenticate(username=serializer.data.get("login"),
                        password=serializer.data.get("password"))
    if user is None:
        return Response({"success": 0, "error": "Wrong login or password"}, status=401)

    try:
        token = Token.objects.get(user=user)
    except ObjectDoesNotExist:
        return Response({"success": 0, "error": "There is user that incorrect created"}, status=500)

    return Response(
        {"success": 1, "token": token.key},
        status=200
    )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def change_password(request):
    serializer = ChangePasswordSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = request.user
    user.set_password(serializer.data.get("password"))
    user.save()
    return Response({"success": 1}, status=200)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def change_creds(request):
    serializer = ChangeCredsSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = request.user
    user.name = serializer.data.get("name")
    user.surname = serializer.data.get("surname")
    user.save()
    return Response({"success": 1}, status=200)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def current_user(request):
    user = request.user
    return Response({
        'username': user.username,
        'name': user.name,
        'surname': user.surname,
        'role': user.role
    })


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_curses(request):
    user = request.user
    return Response({

    })


@api_view(["GET"])
@permission_classes([AllowAny])
def show_course(request, *args, **kwargs):
    try:
        course = Course.objects.get(pk=kwargs.get("pk", None))
    except:
        return Response({"Error: Object doesn't exist"})

    return Response({'name': course.name,
                     'description': course.description,
                     'status': course.status,
                     'available': course.available,
                     'date_of_adt': course.date_of_adt,
                     'date_of_start': course.date_of_start,
                     'date_of_end': course.date_of_end})


# @api_view(["GET"])
# @permission_classes([IsAuthenticated])
# def show_course_auth(request, *args, **kwargs):
#     try:
#         course = Course.objects.get(pk=kwargs.get("pk", None))
#         user = AdditionalUserInfo.objects.get(user=request.user)
#
#     except:
#         return Response({"Error: Object doesn't exist"})
#
#     return Response({'role': user.roles,
#                      'teachers': course.users(roles=),
#                      'program': course.program})


# @api_view(["GET"])
# @permission_classes([IsAdmin, IsTeacher])
# def show_course_admin(request, *args, **kwargs):
#     try:
#         course = Course.objects.get(pk=kwargs.get("pk", None))
#         user = AdditionalUserInfo.objects.get(user=request.user)
#
#     except:
#         return Response({"Error: Object doesn't exist"})
#
#     return Response({'users': course.users})