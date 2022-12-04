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

@api_view(['GET'])
def show_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    context = {'name': course.name,
               'description': course.description,
               'status': course.status,
               'lecturers': course.lecturers,
               'date_of_adt': course.date_of_adt,
               'date_of_start': course.date_of_start,
               'date_of_end': course.date_of_end}

    if request.user is not None:
        role = CourseUser.objects.filter(global_account=request.user).roles.name    # что-то не так с roles
        global_role = AdditionalUserInfo.objects.filter(user=request.user)

        context += {'available': course.available,
                    'role': role}

        if role is not None and global_role is not None:
            context += {'program': course.program,
                        'materials': course.materials}

            if role == "lead" or global_role == "lecturer" or global_role == "admin":
                context += {'students': course.students}

    return Response({'course': context})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def member_course(request, course_id):
    pass


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def edit_course(request, course_id):
    if request.user is not None:
        course = get_object_or_404(Course, pk=course_id)
        role = CourseUser.objects.filter(global_account=request.user).roles.name  # что-то не так с roles
        global_role = AdditionalUserInfo.objects.filter(user=request.user)

        if role == "lecturer":
            serializer = CourseInfoSerializer(data=request.data['students'], instance=course)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({'course': serializer.data})

        if global_role == "admin":
            serializer = CourseInfoSerializer(data=request.data, instance=course)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({'course': serializer.data})

    return Response({'error': 'Permission denied'})
