from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from .serializers import DealWithCourseSerializer
from django.contrib.auth.models import User
# from ..models import Course

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def course_deal(request):
    user = request.user
    serializer = DealWithCourseSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user_deal = serializer.data.get("user_deal")
    # if (user_deal == 1):
    #   course = Course.get(request.data.get("course_title"))
    #   try:
    #       course.add_member(user)
    #   except NoAbleAddMember:
    #       return Response({"success": 0}, "error": "Not able to add member"}, status=450)
    # if (user_deal == -1):
    #   course = Course.get(request.data.get("course_title"))
    #   try:
    #       course.delete_member(user)
    #   except NoAbleAddMember:
    #       return Response({"success": 0}, "error": "Not able to delete member"}, status=451)
    return Response({"success": 1}, status=200)


@api_view(["GET"])
@permission_classes([AllowAny])
def course(request):
    # course = Course.get(request.data.get("course_title"))
    return Response({
        # 'course_title': Course.title
        # ...
    })

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def course_for_auth(request):
    # course = Course.get(request.data.get("course_title"))

    return Response({
        # 'course_user_role': Course.user_role
        # 'course_materials': Course.materials  это будет ссылкой на новую страницу
    })