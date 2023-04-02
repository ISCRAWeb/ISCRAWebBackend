from rest_framework import serializers
from .models import Course


class LoginSerializer(serializers.Serializer):
    login = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

class ChangePasswordSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class ChangeCredsSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100)
    surname = serializers.CharField(max_length=100)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

class CourseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['__all__']


# class CourseEditSerializer(serializers.Serializer):
#     name = serializers.CharField()
#     description = serializers.CharField()
#     status = serializers.IntegerField()
#     available = serializers.BooleanField(default=False)
#     lecturers = serializers.ListField()
#     students = serializers.ListField()
#     program = serializers.ListField(child=serializers.CharField())
#     materials = serializers.ListField(child=serializers.FileField())
#
#     date_of_start = serializers.DateTimeField()
#     date_of_end = serializers.DateTimeField()
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.status = validated_data.get('status', instance.status)
#         instance.available = validated_data.get('available', instance.available)
#         instance.lecturers = validated_data.get('lecturers', instance.lecturers)
#         instance.students = validated_data.get('students', instance.students)
#         instance.program = validated_data.get('program', instance.program)
#         instance.materials = validated_data.get('materials', instance.materials)
#         instance.date_of_start = validated_data.get('date_of_start', instance.date_of_start)
#         instance.date_of_end = validated_data.get('date_of_end', instance.date_of_end)
#         instance.save()
#         return instance
#
#     def delete(self, course_id):
#         Course.objects.delete(pk=course_id)
#
#         return
